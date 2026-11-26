"""Spectral library entropy search

Query an indexed library with a synthetic peptide fragment spectrum.

Li and Fiehn, Flash entropy search (2023)
https://doi.org/10.1038/s41592-023-02012-9
MS Entropy, library search interface
https://msentropy.readthedocs.io/en/latest/"""

from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
import numpy as np
import matplotlib.pyplot as plt

from peptide_methods import fragments, RESIDUES, PROTON, WATER
from ms_entropy import FlashEntropySearch


def main():
    seqs = ["PEPTIDE", "PEPTEDI", "TIDEPEP", "ADGLKVR"]

    def entry(seq):
        b, y = fragments(seq)
        mzs = np.r_[b, y]
        intens = np.r_[np.linspace(1, 3, len(b)), np.linspace(3, 2, len(y))]
        order = np.argsort(mzs)
        return {
            "precursor_mz": (sum(RESIDUES[c] for c in seq) + WATER + 2 * PROTON) / 2,
            "peaks": np.column_stack((mzs[order], intens[order])).astype(np.float32),
            "label": seq,
        }

    lib = [entry(seq) for seq in seqs]
    engine = FlashEntropySearch(max_ms2_tolerance_in_da=0.03)
    indexed = engine.build_index(lib, clean_spectra=True)
    q = entry(seqs[0])
    q["peaks"][:, 0] += 0.001
    scores = engine.search(
        q["precursor_mz"],
        q["peaks"],
        ms1_tolerance_in_da=0.01,
        ms2_tolerance_in_da=0.015,
        method="identity",
        precursor_ions_removal_da=None,
    )["identity_search"]
    labels = [spec["label"] for spec in indexed]
    print("scores", dict(zip(labels, np.round(scores, 4).tolist())))
    assert labels[int(np.argmax(scores))] == seqs[0]
    fig, ax = plt.subplots(figsize=(6.3, 3), constrained_layout=True)
    ax.bar(labels, scores, color="teal")
    ax.set(ylabel="Entropy similarity", ylim=(0, 1.08), title="Precursor-gated library search")
    plt.show()


if __name__ == "__main__":
    main()
