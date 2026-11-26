"""Smith-Waterman Local Alignment

Find the best matching substrings without paying for unrelated flanks.

Smith and Waterman, local alignment (1981)
https://doi.org/10.1016/0022-2836(81)90087-5
Biopython, pairwise alignments
https://biopython.org/docs/latest/Tutorial/chapter_pairwise.html"""

from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
import numpy as np
import matplotlib.pyplot as plt

from genome_methods import dp_align, show_dp
from Bio.Align import PairwiseAligner


def main():
    a, b = ("TTGACCTGAA", "CCGACCTCAA")
    score, left, right, matrix, path = dp_align(a, b, local=True)
    check = PairwiseAligner(
        mode="local", match_score=2, mismatch_score=-1, open_gap_score=-2, extend_gap_score=-2
    )
    print(left)
    print(right)
    print("Traceback score", score, "| independent score", check.score(a, b))
    assert score == check.score(a, b)
    show_dp(a, b, matrix, path)
    plt.show()


if __name__ == "__main__":
    main()
