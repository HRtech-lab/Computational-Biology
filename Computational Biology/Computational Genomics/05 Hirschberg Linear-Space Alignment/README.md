# Hirschberg Linear-Space Alignment

Recover one complete global alignment while keeping rolling score rows.

Split the first sequence at its middle. Forward and reverse row scores identify an optimal split in the second sequence. Recursive calls recover the two halves. The plot counts score buffers, excluding output strings, recursion and Python slicing overhead.

[Worked notebook](hirschberg_linear_space_alignment.ipynb) · [Python script](hirschberg_linear_space_alignment.py)

## Worked example

Run the example from top to bottom. The printed check and figure use the same observations.

## Recorded output

```text
GACTCTGAAG
GA-TCTGACG
Alignment score 13
```

## Interpreting the result

The alignment score agrees with full traceback. Different tie rules can produce a different optimal alignment.

![Hirschberg Linear-Space Alignment, worked result](figure.svg)

## Exercise

Build two sequences with several equally good gap positions and check the score for each traceback.

## References

[Hirschberg, a linear-space alignment algorithm (1975)](https://doi.org/10.1145/360825.360861)

[Needleman and Wunsch, global alignment (1970)](https://doi.org/10.1016/0022-2836(70)90057-4)
