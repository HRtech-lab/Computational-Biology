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
| NetworkX | K-mer graph drawing | [NetworkX licence](https://networkx.org/documentation/stable/license.html) |
| NumPy, SciPy, Matplotlib, scikit-learn | Numerical operations, independent references and visualisation | [NumPy](https://numpy.org/doc/stable/license.html) · [SciPy](https://github.com/scipy/scipy) · [Matplotlib](https://matplotlib.org/stable/project/license.html) · [scikit-learn](https://github.com/scikit-learn/scikit-learn) |

The examples generate short base strings, symbolic variants, anonymous synthetic genotypes, short peptide standards, ion intensities and coordinate clouds. No external reference genome, protein structure, patient record, spectrum archive or trained model is packaged. The notebooks show exactly which generator or explicit literal produced their observations. Primary sources for each method appear beside the relevant derivation and code.
