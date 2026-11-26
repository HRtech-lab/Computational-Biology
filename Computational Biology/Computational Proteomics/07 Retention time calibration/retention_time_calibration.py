"""Retention time calibration

Map observed retention times to a common scale using standards.

scikit-learn, isotonic regression
https://scikit-learn.org/stable/modules/isotonic.html"""

from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
import numpy as np
import matplotlib.pyplot as plt

from sklearn.isotonic import IsotonicRegression


def main():
    t = np.arange(1.0, 20.0)
    lab = t + 0.018 * t * t + 0.15 * np.sin(t)
    train = np.arange(len(t)) % 2 == 0
    fit = IsotonicRegression(out_of_bounds="clip").fit(lab[train], t[train])
    pred = fit.predict(lab[~train])
    before = np.mean(abs(lab[~train] - t[~train]))
    after = np.mean(abs(pred - t[~train]))
    print(f"held-out MAE before {before:.3f} min | after {after:.3f} min")
    assert after < before
    fig, ax = plt.subplots(figsize=(6, 3.3), constrained_layout=True)
    ax.scatter(lab[train], t[train], label="Calibration")
    ax.scatter(lab[~train], t[~train], marker="x", label="Held out")
    ax.plot(lab, fit.predict(lab), color="0.45", label="Monotone map")
    ax.set(xlabel="Run time (min)", ylabel="Reference time (min)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
