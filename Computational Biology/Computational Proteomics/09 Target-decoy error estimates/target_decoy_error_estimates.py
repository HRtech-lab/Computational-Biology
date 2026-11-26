"""Target-decoy error estimates

Convert a list of competing target and decoy wins into score-level q-values.

Elias and Gygi, target-decoy search (2007)
https://doi.org/10.1038/nmeth1019"""

from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
import numpy as np
import matplotlib.pyplot as plt

from peptide_methods import qvalues


def main():
    score = np.array([98, 96, 94, 92, 90, 89, 88, 87, 85, 85, 83, 81, 80, 78, 76, 74])
    decoy = np.isin(np.arange(len(score)), [8, 11, 14])
    s, f, q = qvalues(score, decoy)
    assert np.all(np.diff(q) >= -1e-12) and np.all(q <= f + 1e-12)
    print("score  estimate  q-value")
    print(np.column_stack([s, f, q])[::2].round(3))
    fig, ax = plt.subplots(figsize=(6.4, 3.2), constrained_layout=True)
    ax.step(s, f, where="post", label="Threshold FDR")
    ax.step(s, q, where="post", label="q-value")
    ax.invert_xaxis()
    ax.set(xlabel="Score threshold (decreasing)", ylabel="Estimated fraction")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
