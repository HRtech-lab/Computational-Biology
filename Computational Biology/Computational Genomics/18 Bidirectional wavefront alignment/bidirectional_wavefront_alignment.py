"""Bidirectional wavefront alignment

Run BiWFA from WFA2-lib on sequence pairs with known edits and verify its cost with an independent dynamic programme.

Marco-Sola et al., optimal gap-affine alignment in O(s) space
https://doi.org/10.1093/bioinformatics/btad074
WFA2-lib, installation and memory modes
https://github.com/smarco/WFA2-lib"""

from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
import numpy as np
import matplotlib.pyplot as plt

from tempfile import TemporaryDirectory
import shutil, subprocess, re
from genome_methods import gotoh, rng_dna


def main():
    rng = np.random.default_rng(19)
    base = rng_dna(rng, 90)
    pairs = [
        (base, base),
        (base, base[:30] + "GGG" + base[30:]),
        (base, base[:45] + base[50:]),
        (base, base[:12] + "TTAC" + base[16:]),
        (base, base[:20] + base[23:51] + "ATTT" + base[51:]),
    ]
    binary = shutil.which("align_benchmark")
    if not binary:
        raise FileNotFoundError("Build WFA2-lib and add its bin directory to PATH")
    with TemporaryDirectory() as temp:
        work = Path(temp)
        inp = work / "pairs.seq"
        out = work / "scores.tsv"
        inp.write_text("".join(f">{a}\n<{b}\n" for a, b in pairs))
        subprocess.run(
            [
                binary,
                "-a",
                "gap-affine-wfa",
                "--wfa-memory",
                "ultralow",
                "--wfa-heuristic",
                "none",
                "-g",
                "0,2,3,1",
                "-i",
                str(inp),
                "-o",
                str(out),
                "-q",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        records = [line.split() for line in out.read_text().splitlines()]
    native = [-int(row[0]) for row in records]
    exact = [gotoh(a, b)[0] for a, b in pairs]
    assert native == exact
    for i, (score, cigar) in enumerate(records):
        print(f"pair {i+1}: cost {-int(score)}, CIGAR {cigar}")
    fig, ax = plt.subplots(figsize=(6.4, 3), constrained_layout=True)
    ix = np.arange(len(pairs))
    ax.bar(ix, native, color="teal", label="BiWFA")
    ax.plot(ix, exact, "_", ms=16, color="sienna", label="Gotoh")
    ax.set(
        xticks=ix,
        xticklabels=["Identical", "Insert", "Delete", "Replace", "Mixed"],
        ylabel="Optimal affine cost",
    )
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
