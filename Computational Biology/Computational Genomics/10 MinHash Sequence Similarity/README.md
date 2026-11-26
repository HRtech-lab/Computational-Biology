# MinHash Sequence Similarity

Estimate k-mer set similarity from the minimum keys across repeated random orderings.

For a uniformly random ordering, the minimum of two nonempty sets agrees with probability equal to their Jaccard similarity. The tiny observed universe here permits exact random permutations. Practical sequence sketchers use hashes and more economical sketches.

[Worked notebook](minhash_sequence_similarity.ipynb) · [Python script](minhash_sequence_similarity.py)

## Worked example

Run the example from top to bottom. The printed check and figure use the same observations.

## Recorded output

```text
Exact Jaccard 0.819 | 400-sketch estimate 0.820
```

## Interpreting the result

The estimate fluctuates even with unchanged sequences. Finite sketch error and biological sampling error are separate.

![MinHash Sequence Similarity, worked result](figure.svg)

## Exercise

Compare variation across seeds at sketch sizes 20 and 400.

## References

[Ondov et al., Mash (2016)](https://doi.org/10.1186/s13059-016-0997-x)
