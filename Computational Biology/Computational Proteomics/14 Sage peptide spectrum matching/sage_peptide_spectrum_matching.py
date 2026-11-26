"""Sage peptide spectrum matching

Identify which synthetic peptide produced each artificial tandem mass spectrum, using the public Sage search engine.

Lazear, Sage search and quantification (2023)
https://doi.org/10.1021/acs.jproteome.3c00486
Sage configuration and inputs
https://sage-docs.vercel.app/docs/configuration
OpenMS Python bindings
https://pyopenms.readthedocs.io/"""

from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
import numpy as np
import matplotlib.pyplot as plt

from tempfile import TemporaryDirectory
from sage_fixture import search


def main():
    with TemporaryDirectory() as work:
        truth, rows = search(work)
    counts = {"Correct": 0, "Other target": 0, "Decoy": 0, "Unreported": len(truth)}
    seen = set()
    for row in rows:
        scan = row["scannr"]
        assert scan in truth and scan not in seen
        seen.add(scan)
        counts["Unreported"] -= 1
        key = (
            "Decoy"
            if int(row["label"]) < 0
            else "Correct" if row["peptide"] == truth[scan] else "Other target"
        )
        counts[key] += 1
    print("Known spectra", len(truth))
    print(counts)
    print("correct fraction of all spectra", round(counts["Correct"] / len(truth), 3))
    assert counts["Correct"] >= 0.9 * len(truth)
    fig, ax = plt.subplots(figsize=(6.3, 3.1), constrained_layout=True)
    ax.bar(counts.keys(), counts.values(), color=["teal", "sienna", "slategray", "silver"])
    ax.set(ylabel="Spectra", title="Search winners against known identities")
    plt.show()


if __name__ == "__main__":
    main()
