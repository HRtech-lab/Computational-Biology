# Computational Proteomics

A spectrum records ion intensity by mass-to-charge ratio. Identifying a peptide requires a model that relates a sequence to possible ions. Quantifying a protein across samples requires further choices about peak areas, peptide ambiguity and missing observations. This course keeps those questions separate and measures each against a small known fixture.

## Reading tandem mass spectra

The digestion and mass lessons introduce residue masses, water, charge and the two fragment series. A profile-level experiment shows why centroiding is a measurement step. Extracted ion chromatograms and retention calibration show how much depends on the acquisition window. Flash entropy search compares a query against a synthetic library. The Sage lesson searches 80 known synthetic spectra against a FASTA file that the script creates locally.

![Mass and fragment ions](02%20Mass%20and%20fragment%20ions/figure.svg)

## Inference and uncertainty

A strong peptide-spectrum score is one piece of evidence. Learn how competing target and decoy hits lead to score-level q-values, how multiple proteins can explain the same observed peptides, and how missing intensities affect sample-to-sample ratios. The MaxLFQ lecture recovers known relative log-abundances and records the connectivity assumption. The final statistical exercise reports both discoveries and incorrect calls because its ground truth is constructed.

## Worked lectures

| Lecture | Question or experiment |
|---|---|
| [01. In silico peptide digestion](01%20In%20silico%20peptide%20digestion/README.md) | Enumerate the products of trypsin cleavage in a short invented sequence. |
| [02. Mass and fragment ions](02%20Mass%20and%20fragment%20ions/README.md) | Calculate a neutral monoisotopic mass and locate the b and y fragment series. |
| [03. Protein alignment with BLOSUM62](03%20Protein%20alignment%20with%20BLOSUM62/README.md) | Score conservative substitutions in a local peptide alignment. |
| [04. Carbon isotope envelopes](04%20Carbon%20isotope%20envelopes/README.md) | Calculate nominal isotope probabilities for a carbon-only model. |
| [05. Centroiding profile spectra](05%20Centroiding%20profile%20spectra/README.md) | Recover peak positions from an artificial profile-mode spectrum. |
| [06. Extracted ion chromatograms](06%20Extracted%20ion%20chromatograms/README.md) | Estimate the area of a chromatographic peak with a known generating curve. |
| [07. Retention time calibration](07%20Retention%20time%20calibration/README.md) | Map observed retention times to a common scale using standards. |
| [08. Spectral library entropy search](08%20Spectral%20library%20entropy%20search/README.md) | Query an indexed library with a synthetic peptide fragment spectrum. |
| [09. Target-decoy error estimates](09%20Target-decoy%20error%20estimates/README.md) | Convert a list of competing target and decoy wins into score-level q-values. |
| [10. Protein group parsimony](10%20Protein%20group%20parsimony/README.md) | Find every smallest protein set consistent with observed peptides. |
| [11. MaxLFQ relative abundance](11%20MaxLFQ%20relative%20abundance/README.md) | Recover sample-level protein changes despite unequal peptide responses and missing values. |
| [12. Kabsch structural superposition](12%20Kabsch%20structural%20superposition/README.md) | Align two sets of matched synthetic coordinates while preserving handedness. |
| [13. Differential abundance and multiplicity](13%20Differential%20abundance%20and%20multiplicity/README.md) | Test changes across replicate samples and compare raw and adjusted significance. |
| [14. Sage peptide spectrum matching](14%20Sage%20peptide%20spectrum%20matching/README.md) | Identify which synthetic peptide produced each artificial tandem mass spectrum, using the public Sage search engine. |

See the [environment and source notes](../../README.md) for dependencies and native tools. [MIT licence](../../LICENSE)
