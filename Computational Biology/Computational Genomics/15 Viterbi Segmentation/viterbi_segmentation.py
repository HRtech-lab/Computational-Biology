"""Viterbi Segmentation

Infer a hidden low- or high-GC state from a sequence of binary observations.

Rabiner, hidden Markov models (1989)
https://doi.org/10.1109/5.18626"""

from pathlib import Path
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
import numpy as np
import matplotlib.pyplot as plt

from scipy.special import logsumexp


def main():
    rng = np.random.default_rng(17)
    truth = np.repeat([0, 1, 0, 1], [34, 33, 27, 26])
    em = np.array([[0.80, 0.20], [0.18, 0.82]])
    x = np.array([rng.choice(2, p=em[s]) for s in truth])
    transition = np.log([[0.96, 0.04], [0.04, 0.96]])
    v = np.log([0.5, 0.5]) + np.log(em[:, x[0]])
    f = v.copy()
    back = []
    for obs in x[1:]:
        scores = v[:, None] + transition
        back.append(scores.argmax(0))
        v = scores.max(0) + np.log(em[:, obs])
        f = logsumexp(f[:, None] + transition, axis=0) + np.log(em[:, obs])
    path = [int(v.argmax())]
    for bp in reversed(back):
        path.append(int(bp[path[-1]]))
    path = np.array(path[::-1])
    assert v.max() <= logsumexp(f) + 1e-9
    print(
        f"State accuracy {(path==truth).mean():.3f} | best-path log probability {v.max():.2f} | observation log likelihood {logsumexp(f):.2f}"
    )
    plt.figure(figsize=(7.2, 2.8))
    plt.imshow(np.stack([x, truth, path]), aspect="auto", interpolation="nearest", cmap="cividis")
    plt.yticks([0, 1, 2], ["Observed GC", "True state", "Viterbi"])
    plt.xlabel("Position")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
