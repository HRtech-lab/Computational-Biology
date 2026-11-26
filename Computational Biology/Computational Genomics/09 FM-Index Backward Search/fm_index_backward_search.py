"""FM-Index Backward Search

Count and locate exact substring matches by narrowing an interval in suffix-array order.

Ferragina and Manzini, opportunistic indexing (2000)
https://doi.org/10.1109/SFCS.2000.892127"""

from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
import numpy as np
import matplotlib.pyplot as plt

from genome_methods import fm_index, backward


def main():
    text = "GATTACAGATTAGATACA"
    query = "GAT"
    index = fm_index(text)
    hits, width = backward(query, index)
    assert hits == [i for i in range(len(text)) if text.startswith(query, i)]
    print("BWT", index[1])
    print("Zero-based matches", hits)
    print("Widths", width)
    plt.figure(figsize=(6.1, 3))
    plt.step(range(len(width)), width, where="mid")
    plt.scatter(range(len(width)), width)
    plt.xticks(range(len(width)), ["empty"] + [query[-i:] for i in range(1, len(query) + 1)])
    plt.ylabel("Candidate suffixes")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
