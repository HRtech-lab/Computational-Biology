"""Gotoh Affine Gaps

Opening a gap and extending an existing gap can carry different costs. Three dynamic-programming states remember which operation ended the aligned prefix.

Gotoh, affine gap alignment (1982)
https://doi.org/10.1016/0022-2836(82)90398-9
Biopython, pairwise alignments
https://biopython.org/docs/latest/Tutorial/chapter_pairwise.html"""

from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
import numpy as np
import matplotlib.pyplot as plt

from genome_methods import gotoh
from Bio.Align import PairwiseAligner


def main():
    a, b = "ACGTTTTTAC", "ACGTAC"
    cost, H, D, I = gotoh(a, b)
    check = PairwiseAligner(
        mode="global", match_score=0, mismatch_score=-2, open_gap_score=-4, extend_gap_score=-1
    )
    assert cost == -check.score(a, b)
    print("Optimal cost", cost, "| length-one gap costs 4")
    fig, axes = plt.subplots(1, 3, figsize=(8.8, 3), constrained_layout=True)
    for ax, m, title in zip(axes, [H, D, I], ["Best cost", "Gap in B", "Gap in A"]):
        ax.imshow(np.ma.masked_invalid(m), aspect="auto", cmap="viridis")
        ax.set(title=title, xlabel="B prefix", ylabel="A prefix")
    plt.show()


if __name__ == "__main__":
    main()
