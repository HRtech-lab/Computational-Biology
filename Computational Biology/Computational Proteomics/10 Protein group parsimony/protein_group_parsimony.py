"""Protein group parsimony

Find every smallest protein set consistent with observed peptides.

Nesvizhskii and Aebersold, protein inference (2005)
https://doi.org/10.1074/mcp.R500012-MCP200"""

from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
import numpy as np
import matplotlib.pyplot as plt

from peptide_methods import parsimony


def main():
    mapping = {"A": {"p1", "p2"}, "B": {"p2", "p3"}, "C": {"p1", "p2"}, "D": {"p4"}}
    obs = {"p1", "p2", "p3", "p4"}
    sol = parsimony(mapping, obs)
    print("minimum explanations", sol)
    assert sol == [("A", "B", "D"), ("B", "C", "D")]
    fig, ax = plt.subplots(figsize=(5.4, 3), constrained_layout=True)
    p = sorted(obs)
    ax.imshow([[x in mapping[k] for x in p] for k in mapping], cmap="Blues", vmin=0, vmax=1)
    ax.set(
        xticks=range(len(p)),
        xticklabels=p,
        yticks=range(len(mapping)),
        yticklabels=list(mapping),
        xlabel="Observed peptide",
        ylabel="Candidate protein",
    )
    plt.show()


if __name__ == "__main__":
    main()
