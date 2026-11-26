"""In silico peptide digestion

Enumerate the products of trypsin cleavage in a short invented sequence.

ExPASy PeptideCutter, cleavage rules
https://web.expasy.org/peptide_cutter/peptidecutter_enzymes.html"""

from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
import numpy as np
import matplotlib.pyplot as plt

from peptide_methods import digest


def main():
    seq = "AGKTPRPAQKVLRT"
    rows = digest(seq, 1)
    print("start  end  peptide")
    for a, b, s in rows:
        print(f"{a:5d}{b:5d}  {s}")
    assert "".join(s for _, _, s in digest(seq)) == seq and "TPRPAQK" in [s for _, _, s in rows]
    fig, ax = plt.subplots(figsize=(7, 3.3), constrained_layout=True)
    for j, (a, b, s) in enumerate(rows):
        ax.plot([a + 0.08, b - 0.08], [j, j], lw=5)
        ax.text((a + b) / 2, j + 0.12, s, ha="center", fontsize=8)
    ax.set(
        xlabel="Residue boundary (zero-based)",
        yticks=[],
        ylim=(-0.5, len(rows)),
        title="Peptides allowing one missed cleavage",
    )
    plt.show()


if __name__ == "__main__":
    main()
