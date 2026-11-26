"""Generate synthetic peptide spectra and run the local Sage proteomics executable."""

import csv
import json
import os
from pathlib import Path
import shutil
import subprocess
import numpy as np
from pyopenms import MSExperiment, MSSpectrum, MzMLFile, Precursor, SpectrumSettings
from peptide_methods import PROTON, WATER, RESIDUES, fragments


def search(work, seed=37):
    work = Path(work)
    binary = shutil.which("sage")
    if not binary:
        raise FileNotFoundError(
            "Install the Sage proteomics release and put its executable on PATH"
        )
    rng = np.random.default_rng(seed)
    peptides = []
    while len(peptides) < 80:
        s = "".join(rng.choice(list("AGVFPSTDNQEL"), size=11)) + "K"
        if s not in peptides:
            peptides.append(s)
    fasta = work / "standards.fasta"
    fasta.write_text("".join(f">standard_{i}\n{s}\n" for i, s in enumerate(peptides)))
    experiment = MSExperiment()
    truth = {}
    for i, peptide in enumerate(peptides):
        scan = f"scan={i+1}"
        spectrum = MSSpectrum()
        spectrum.setMSLevel(2)
        spectrum.setRT(8.0 * (i + 1))
        spectrum.setNativeID(scan)
        spectrum.setType(SpectrumSettings.SpectrumType.CENTROID)
        neutral = WATER + sum(RESIDUES[a] for a in peptide)
        precursor = Precursor()
        precursor.setMZ((neutral + 2 * PROTON) / 2)
        precursor.setCharge(2)
        spectrum.setPrecursors([precursor])
        b, y = fragments(peptide)
        signal = np.concatenate([b, y])
        noise = rng.uniform(120, 1150, 18)
        mz = np.r_[signal * (1 + rng.normal(0, 1.0e-6, len(signal))), noise]
        intensity = np.r_[
            rng.uniform(800, 2000, len(signal)), rng.uniform(5, 80, len(noise))
        ]
        order = np.argsort(mz)
        spectrum.set_peaks((mz[order], intensity[order]))
        experiment.addSpectrum(spectrum)
        truth[scan] = peptide
    raw = work / "classroom.mzML"
    MzMLFile().store(str(raw), experiment)
    config = {
        "database": {
            "fasta": str(fasta),
            "enzyme": {"missed_cleavages": 0},
            "min_ion_index": 1,
        },
        "precursor_tol": {"ppm": [-10, 10]},
        "fragment_tol": {"ppm": [-15, 15]},
        "isotope_errors": [0, 0],
        "predict_rt": False,
        "report_psms": 1,
    }
    param = work / "search.json"
    param.write_text(json.dumps(config))
    subprocess.run(
        [
            binary,
            "--disable-telemetry-i-dont-want-to-improve-sage",
            "-o",
            str(work),
            str(param),
            str(raw),
        ],
        env=dict(os.environ, RAYON_NUM_THREADS="1"),
        check=True,
        capture_output=True,
        text=True,
        timeout=90,
    )
    with (work / "results.sage.tsv").open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    return truth, rows
