# Sources, software and data

The teaching implementations and synthetic fixtures were written for this collection. Package APIs and native executables are called as installed dependencies. An algorithm citation identifies the method. The separate licence link describes reuse of the upstream implementation.

| Component | Use in the lessons | Upstream source and licence |
|---|---|---|
| Biopython | BLOSUM62 through its installed matrix loader and independent alignment checks | [Project and licensing](https://github.com/biopython/biopython/blob/master/LICENSE.rst) |
| Edlib | Independent check of exact edit distance | [Edlib](https://github.com/Martinsos/edlib) |
| Minimap2 and mappy | Native mapper on synthetic reads | [Minimap2 licence](https://github.com/lh3/minimap2/blob/master/LICENSE.txt) |
| WFA2-lib | Native bidirectional affine alignment | [WFA2-lib](https://github.com/smarco/WFA2-lib) |
| OpenMS and pyOpenMS | Profile peak picking and mzML generation | [OpenMS](https://github.com/OpenMS/OpenMS) |
| Pyteomics | Monoisotopic residue masses and mass checks | [Pyteomics](https://github.com/levitsky/pyteomics) |
| MS Entropy | Indexed entropy search of classroom spectra | [MSEntropy](https://github.com/YuanyueLi/MSEntropy) |
| Sage | Native target-decoy peptide-spectrum search | [Sage](https://github.com/lazear/sage) |
| NCBI BLAST+ | Local nucleotide database construction and search | [NCBI BLAST+ distribution](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/) · [NCBI software and data policies](https://www.ncbi.nlm.nih.gov/home/about/policies/) |
| MAFFT | Multiple sequence alignment | [MAFFT distribution and licence](https://mafft.cbrc.jp/alignment/software/) |
| Foldseek | Native 3Di structural alignment and scores | [Foldseek source and licence](https://github.com/steineggerlab/foldseek) |
| NetworkX | K-mer graph drawing | [NetworkX licence](https://networkx.org/documentation/stable/license.html) |
| NumPy, SciPy, Matplotlib, scikit-learn | Numerical operations, independent references and visualisation | [NumPy](https://numpy.org/doc/stable/license.html) · [SciPy](https://github.com/scipy/scipy) · [Matplotlib](https://matplotlib.org/stable/project/license.html) · [scikit-learn](https://github.com/scikit-learn/scikit-learn) |

The examples generate short base strings, symbolic variants, anonymous synthetic genotypes, short peptide standards, ion intensities and coordinate clouds. The Foldseek chapter includes a selected coordinate file from PDB 1UBQ. Chain A N, Cα, C, O and Cβ records were retained from the deposition by Vijay-Kumar, Bugg and Cook. The coordinates are under the wwPDB CC0 1.0 dedication. The teaching code, plotted controls and figure were produced in the chapter. [PDB 1UBQ](https://www.rcsb.org/structure/1UBQ) · [Original structure paper](https://doi.org/10.1016/0022-2836(87)90679-6) · [wwPDB data terms](https://www.wwpdb.org/about/usage-policies) The notebooks show exactly which generator or explicit literal produced their observations. Primary sources for each method appear beside the relevant derivation and code.
