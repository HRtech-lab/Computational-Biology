# Computational Genomics

Start with sequence composition and end-to-end alignment. Trace a global alignment, then change the question to local similarity or affine gap costs. Equal scores can correspond to different optimal paths. The lessons compare the scores under a stated convention and check traceback where relevant.

## From dynamic programming to indexing

A dynamic-programming matrix answers a pairwise question. Hirschberg reduces traceback working space by splitting the problem, Myers packs edit states into machine-word operations, and wavefront alignment tracks progress by edit cost. Indexing addresses repeated queries: minimisers select a subset of k-mers, while an FM-index narrows a suffix-array interval one character at a time. The Minimap2 example evaluates mapping coordinates against known origins.

![Needleman-Wunsch Global Alignment](02%20Needleman-Wunsch%20Global%20Alignment/figure.svg)

## From reads to population summaries

The de Bruijn lesson reconstructs a classroom string from a multiset of k-mers. The statistics lessons distinguish alleles from genotypes, show what PCA axes can and cannot identify, trace a Viterbi path and compute linkage disequilibrium from phased counts. All sequences and observations used here are constructed, and no external sequence database is downloaded.

The bidirectional wavefront lecture runs BiWFA using WFA2-lib's ultralow-memory mode with pruning disabled. It checks five native results against a separate Gotoh implementation. BiWFA, Edlib and Minimap2 solve different alignment or mapping problems. A database-search lecture then recovers query intervals and strand using BLAST+. The MAFFT lecture inspects column occupancy and agreement in a four-sequence alignment. These are different evaluation objectives.

## Worked lectures

| Lecture | Question or experiment |
|---|---|
| [01. Sequence composition](01%20Sequence%20composition/README.md) | How much of a sequence is G or C when some bases are unobserved? The denominator matters as much as the numerator. |
| [02. Needleman-Wunsch Global Alignment](02%20Needleman-Wunsch%20Global%20Alignment/README.md) | Align both strings end to end and recover the exact path that earns the score. |
| [03. Smith-Waterman Local Alignment](03%20Smith-Waterman%20Local%20Alignment/README.md) | Find the best matching substrings without paying for unrelated flanks. |
| [04. Gotoh Affine Gaps](04%20Gotoh%20Affine%20Gaps/README.md) | Opening a gap and extending an existing gap can carry different costs. Three dynamic-programming states remember which operation ended the aligned prefix. |
| [05. Hirschberg Linear-Space Alignment](05%20Hirschberg%20Linear-Space%20Alignment/README.md) | Recover one complete global alignment while keeping rolling score rows. |
| [06. Myers Bit-Vector Edit Distance](06%20Myers%20Bit-Vector%20Edit%20Distance/README.md) | Represent one dynamic-programming column with bits and update many pattern positions using integer operations. |
| [07. Affine Wavefront Alignment](07%20Affine%20Wavefront%20Alignment/README.md) | Search by increasing alignment cost and extend exact matches without opening new score levels. |
| [08. Canonical K-mers and Minimisers](08%20Canonical%20K-mers%20and%20Minimisers/README.md) | Select representative k-mers from overlapping windows and keep the same sequence key on either strand. |
| [09. FM-Index Backward Search](09%20FM-Index%20Backward%20Search/README.md) | Count and locate exact substring matches by narrowing an interval in suffix-array order. |
| [10. MinHash Sequence Similarity](10%20MinHash%20Sequence%20Similarity/README.md) | Estimate k-mer set similarity from the minimum keys across repeated random orderings. |
| [11. De Bruijn Graph Traversal](11%20De%20Bruijn%20Graph%20Traversal/README.md) | Reconstruct a short string from its multiset of k-mers using an Eulerian trail. |
| [12. Minimap2 Read Mapping](12%20Minimap2%20Read%20Mapping/README.md) | Run the minimap2 mapper on an artificial reference with known read starts and compare its primary placements with those starts. |
| [13. Genotype Counts and Allele Frequencies](13%20Genotype%20Counts%20and%20Allele%20Frequencies/README.md) | Estimate alternate-allele frequency from diploid genotype calls with missing observations. |
| [14. Population PCA](14%20Population%20PCA/README.md) | Fit axes of genetic variation on simulated training individuals and project independent individuals onto those same axes. |
| [15. Viterbi Segmentation](15%20Viterbi%20Segmentation/README.md) | Infer a hidden low- or high-GC state from a sequence of binary observations. |
| [16. UPGMA Trees](16%20UPGMA%20Trees/README.md) | Reconstruct an ultrametric tree from an artificial distance matrix and compare its implied pair distances with the input. |
| [17. Linkage Disequilibrium](17%20Linkage%20Disequilibrium/README.md) | Measure association between alleles at two loci from known phased chromosome copies. |
| [18. Bidirectional wavefront alignment](18%20Bidirectional%20wavefront%20alignment/README.md) | Run BiWFA from WFA2-lib on sequence pairs with known edits and verify its cost with an independent dynamic programme. |
| [19. BLAST nucleotide database search](19%20BLAST%20nucleotide%20database%20search/README.md) | Locate short fragments in a small local nucleotide database and verify the winning sequence, interval and strand. |
| [20. MAFFT multiple sequence alignment](20%20MAFFT%20multiple%20sequence%20alignment/README.md) | Align four related classroom strings and inspect which columns are shared, variable or sparsely occupied. |

See the [environment and source notes](../../README.md) for dependencies and native tools. [MIT licence](../../LICENSE)
