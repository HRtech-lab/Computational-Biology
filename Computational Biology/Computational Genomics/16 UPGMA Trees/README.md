# UPGMA Trees

Reconstruct an ultrametric tree from an artificial distance matrix and compare its implied pair distances with the input.

Average linkage weights clusters by their number of leaves. Under an ultrametric model, every leaf is the same distance from the root. Linkage heights are pair distances; phylogenetic node heights are half those values.

[Worked notebook](upgma_trees.ipynb) · [Python script](upgma_trees.py)

## Worked example

Run the example from top to bottom. The printed check and figure use the same observations.

## Recorded output

```text
Cophenetic correlation 1.000 | maximum distance error 0.000
```

## Interpreting the result

Exact agreement is expected for this constructed ultrametric matrix. A rate change on a single lineage can break that property.

![UPGMA Trees, worked result](figure.svg)

## Exercise

Change one distance symmetrically and measure the cophenetic error again.

## References

[SciPy, average linkage and UPGMA](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html)
