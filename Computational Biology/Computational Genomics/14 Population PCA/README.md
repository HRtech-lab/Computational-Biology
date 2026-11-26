# Population PCA

Fit axes of genetic variation on simulated training individuals and project independent individuals onto those same axes.

The allele frequencies, centring and scale are estimated from training genotypes only. The usual biallelic scale is the square root of 2p(1−p). Each point represents an artificial observation, and the groups below exist only in the simulation.

[Worked notebook](population_pca.ipynb) · [Python script](population_pca.py)

## Worked example

Run the example from top to bottom. The printed check and figure use the same observations.

## Recorded output

```text
Training variance fractions [0.066 0.027 0.026 0.026]
Held-out individuals 100
```

## Interpreting the result

A principal component axis can be multiplied by minus one with the same fit. Separation depends on marker selection and the simulated frequency difference.

![Population PCA, worked result](figure.svg)

## Exercise

Set every simulated frequency shift to zero and compare the held-out separation.

## References

[Patterson, Price and Reich, population structure and eigenanalysis (2006)](https://doi.org/10.1371/journal.pgen.0020190)
