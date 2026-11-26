"""Carbon isotope envelopes

Calculate nominal isotope probabilities for a carbon-only model.

NIST, atomic weights and isotopic compositions
https://physics.nist.gov/Comp"""

from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import binom


def main():
    k = np.arange(9)
    fig, ax = plt.subplots(figsize=(6.5, 3.2), constrained_layout=True)
    for count in [20, 50, 90]:
        pmf = binom.pmf(k, count, 0.0107)
        ax.plot(k, pmf, "o-", label=f"{count} carbons")
        print(f"C{count} modal offset {k[pmf.argmax()]} | displayed probability {pmf.sum():.6f}")
    assert np.isclose(binom.pmf(np.arange(91), 90, 0.0107).sum(), 1)
    ax.set(
        xlabel="Extra nominal neutron count",
        ylabel="Probability",
        title="Carbon contribution to an isotope envelope",
    )
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
