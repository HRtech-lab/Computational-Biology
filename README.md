# Computational Biology

Two practical courses cover [Computational Genomics](Computational%20Biology/Computational%20Genomics/README.md) and [Computational Proteomics](Computational%20Biology/Computational%20Proteomics/README.md). Each algorithm has a worked example, explicit assumptions and an observable check. Begin with global alignment or peptide digestion, or open the [course directory](Computational%20Biology/README.md).

## Running an example

Use Python 3.12 with the versions in [requirements.txt](requirements.txt). Install them in a virtual environment, launch Jupyter in the repository, and open a notebook from its numbered directory. Alternatively, run the Python script in that directory. Shared implementations sit one level above the chapters in each subject.

Run `python -m unittest -v` from the repository root to check 961 short sequence pairs, tied scores, disconnected samples and mirrored structures.

Five advanced chapters call separately installed native tools. Make their executables available on PATH before running those chapters.

| Lecture | Verified software | Executables |
|---|---|---|
| Bidirectional alignment | [WFA2-lib v2.3.6](https://github.com/smarco/WFA2-lib) | `align_benchmark` from the project's bin directory |
| Local nucleotide database search | [NCBI BLAST+ 2.17.0](https://www.ncbi.nlm.nih.gov/books/NBK279690/) | `makeblastdb`, `blastn` |
| Multiple sequence alignment | [MAFFT 7.526](https://mafft.cbrc.jp/alignment/software/) | `mafft` |
| Peptide-spectrum matching | [Sage proteomics release v0.14.7](https://github.com/lazear/sage/releases) | `sage`; use the proteomics executable |
| Structural alignment | [Foldseek 10.941cd33](https://github.com/steineggerlab/foldseek) | `foldseek` |

The remaining notebooks use the Python dependencies alone. The Sage exercise creates its own mzML and FASTA inputs. The Foldseek exercise includes credited CC0 coordinates from 1UBQ so it can run offline.

## Sources and reuse

The repository's [MIT licence](LICENSE) covers its original code, figures and teaching material. Each lecture cites the algorithm paper or specification and records which public implementation is called. Upstream projects distribute the libraries, native binaries and their manuals under their own terms. The included 1UBQ coordinates carry the wwPDB CC0 dedication. The published figures here come from the chapter scripts. [Dependency and source guide](SOURCES.md)

The [earlier Python collection](https://github.com/HRtech-lab/Computational_Biology_with_Python/tree/archive/before-computational-biology-course) remains available in the repository history.
