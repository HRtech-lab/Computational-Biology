# Minimap2 Read Mapping

Run the minimap2 mapper on an artificial reference with known read starts and compare its primary placements with those starts.

The mapper selects anchors, chains consistent hits and extends them into alignments. The input below deliberately avoids real biological material. A random reference also removes many of the repeats that make real mapping ambiguous.

[Worked notebook](minimap2_read_mapping.ipynb) · [Python script](minimap2_read_mapping.py)

## Worked example

Run the example from top to bottom. The printed check and figure use the same observations.

## Recorded output

```text
Mapped 22/22 | starts within 3 bp 22/22
```

## Interpreting the result

A few terminal errors can be soft-clipped, which shifts the reported start. Mapping quality measures confidence in placement and is different from base quality.

![Minimap2 Read Mapping, worked result](figure.svg)

## Exercise

Copy a long segment to a second reference location and compare the number of primary placements and their mapping qualities.

## References

[Li, Minimap2 (2018)](https://doi.org/10.1093/bioinformatics/bty191)

[Minimap2 Python bindings](https://github.com/lh3/minimap2/tree/master/python)

[Roberts et al., minimisers in biological sequence comparison (2004)](https://doi.org/10.1093/bioinformatics/bth408)
