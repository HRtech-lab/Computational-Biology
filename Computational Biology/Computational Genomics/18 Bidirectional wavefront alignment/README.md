# Bidirectional wavefront alignment

Run BiWFA from WFA2-lib on sequence pairs with known edits and verify its cost with an independent dynamic programme.

BiWFA advances wavefronts from both ends, locates an optimal overlap and reconstructs the alignment by recursion. The ultralow mode implements this strategy. The test disables heuristic pruning and charges 2 for a substitution and 3 plus the gap length for a gap.

[Worked notebook](bidirectional_wavefront_alignment.ipynb) · [Python script](bidirectional_wavefront_alignment.py)

## Compare native and reference costs

Build WFA2-lib v2.3.6 and place its align_benchmark executable on PATH. The input file uses one sequence pair per two lines.

## Recorded output

```text
pair 1: cost 0, CIGAR 90M
pair 2: cost 6, CIGAR 32M3I58M
pair 3: cost 8, CIGAR 45M5D40M
pair 4: cost 4, CIGAR 14M2X74M
pair 5: cost 13, CIGAR 20M3D28M4I39M
```

## Interpreting the result

The cost agrees even when multiple traceback paths are optimal. The short fixture verifies scoring and command configuration. It does not measure a performance crossover.

![Bidirectional wavefront alignment, worked result](figure.svg)

## Exercise

Repeat with a longer gap and predict the marginal cost of each additional base.

## References

[Marco-Sola et al., optimal gap-affine alignment in O(s) space](https://doi.org/10.1093/bioinformatics/btad074)

[WFA2-lib, installation and memory modes](https://github.com/smarco/WFA2-lib)
