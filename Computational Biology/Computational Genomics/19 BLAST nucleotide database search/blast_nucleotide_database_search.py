"""BLAST nucleotide database search

Locate short fragments in a small local nucleotide database and verify the winning sequence, interval and strand.

Altschul et al., BLAST (1990)
https://doi.org/10.1016/S0022-2836(05)80360-2
Camacho et al., BLAST+ (2009)
https://doi.org/10.1186/1471-2105-10-421
NCBI BLAST+ command line manual
https://www.ncbi.nlm.nih.gov/books/NBK279690/"""

from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess, shutil
import numpy as np
import matplotlib.pyplot as plt
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
from genome_methods import rng_dna, rc


def main():
    rng = np.random.default_rng(317)
    subjects = {f"record{i}": rng_dna(rng, 700) for i in range(3)}
    fixtures = [
        ("one", "record0", 110, 180, False),
        ("two", "record1", 275, 355, True),
        ("three", "record2", 302, 376, False),
    ]
    queries = {
        q: (rc(subjects[k][a:b]) if reverse else subjects[k][a:b])
        for q, k, a, b, reverse in fixtures
    }

    def fasta(records):
        return "".join(f">{name}\n{seq}\n" for name, seq in records.items())

    with TemporaryDirectory() as where:
        root = Path(where)
        (root / "subjects.fa").write_text(fasta(subjects))
        (root / "fragments.fa").write_text(fasta(queries))
        subprocess.run(
            ["makeblastdb", "-in", "subjects.fa", "-dbtype", "nucl", "-out", "reference"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
        cmd = [
            "blastn",
            "-task",
            "blastn",
            "-query",
            "fragments.fa",
            "-db",
            "reference",
            "-dust",
            "no",
            "-num_threads",
            "1",
            "-outfmt",
            "6 qseqid sseqid sstart send bitscore evalue",
        ]
        out = subprocess.run(cmd, cwd=root, check=True, capture_output=True, text=True).stdout
    best = {}
    for line in out.splitlines():
        q, k, a, b, score, evalue = line.split()
        if q not in best or float(score) > best[q][3]:
            best[q] = (k, int(a), int(b), float(score), float(evalue))
    fig, ax = plt.subplots(figsize=(7, 3), constrained_layout=True)
    for i, (q, k, a, b, reverse) in enumerate(fixtures):
        hit, start, end, score, evalue = best[q]
        assert hit == k and (start, end) == ((b, a + 1) if reverse else (a + 1, b))
        print(f"{q} -> {hit} {start}..{end}  bits {score:g}  E {evalue:.2g}")
        ax.annotate(
            "",
            xy=(end, i),
            xytext=(start, i),
            arrowprops={"arrowstyle": "-|>", "lw": 3, "color": "#307977"},
        )
    ax.set(
        xlim=(0, 700),
        ylim=(-0.5, 2.5),
        yticks=range(3),
        yticklabels=list(subjects),
        xlabel="Database coordinate (one-based)",
        title="Recovered positions and search orientations",
    )
    plt.show()


if __name__ == "__main__":
    main()
