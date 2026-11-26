# Computational Biology

Two practical courses cover [Computational Genomics](Computational%20Biology/Computational%20Genomics/README.md) and [Computational Proteomics](Computational%20Biology/Computational%20Proteomics/README.md). Each algorithm has a worked example, explicit assumptions and an observable check. Begin with global alignment or peptide digestion, or open the [course directory](Computational%20Biology/README.md).

## Running an example

Use Python 3.12 with the versions in [requirements.txt](requirements.txt). Install them in a virtual environment, launch Jupyter in the repository, and open a notebook from its numbered directory. Alternatively, run the Python script in that directory. Shared implementations sit one level above the chapters in each subject.

Run `python -m unittest -v` from the repository root to check 961 short sequence pairs, tied scores, disconnected samples and mirrored structures.

Two advanced examples call separately installed native programs. For the BiWFA lecture, build WFA2-lib v2.3.6 and put its `bin/align_benchmark` on PATH. For peptide-spectrum matching, install the Sage proteomics release v0.14.7 and put `sage` on PATH. The script creates its own mzML and FASTA files and disables telemetry. The remaining examples need only the Python packages. [WFA2-lib](https://github.com/smarco/WFA2-lib) · [Sage releases](https://github.com/lazear/sage/releases)

## Sources and reuse

The repository's [MIT licence](LICENSE) covers its original code, figures and teaching material. Each lecture cites the algorithm paper or specification and records which public implementation is called. Library code, program binaries, replacement copies of manuals, pretrained weights and third-party datasets are distributed by their own projects. The published figures here come from the chapter scripts. [Dependency and source guide](SOURCES.md)

The [earlier Python collection](https://github.com/HRtech-lab/Computational_Biology_with_Python/tree/archive/before-computational-biology-course) remains available in the repository history.
