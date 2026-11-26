"""Affine Wavefront Alignment

Search by increasing alignment cost and extend exact matches without opening new score levels.

Marco-Sola et al., gap-affine wavefront alignment
https://doi.org/10.1093/bioinformatics/btaa777
WFA2-lib, wavefront and bidirectional modes
https://github.com/smarco/WFA2-lib
Gotoh, affine gap alignment (1982)
https://doi.org/10.1016/0022-2836(82)90398-9"""

from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
import numpy as np
import matplotlib.pyplot as plt

from genome_methods import wavefront, gotoh, rng_dna


def main():
    rng = np.random.default_rng(17)
    a = rng_dna(rng, 80)
    b = a[:24] + "TTT" + a[24:55] + a[58:]
    score, width = wavefront(a, b)
    reference = gotoh(a, b)[0]
    assert score == reference
    print(
        f"Optimal affine cost {score} | active match diagonals across levels {sum(width)} | full grid cells {(len(a)+1)*(len(b)+1)}"
    )
    plt.figure(figsize=(6.2, 3))
    plt.bar(range(len(width)), width, color="#42748b")
    plt.xlabel("Accumulated cost")
    plt.ylabel("Active diagonals")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
