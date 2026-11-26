"""Elementary operations on short classroom peptides and synthetic spectra."""

from itertools import combinations

import numpy as np
from pyteomics import mass

PROTON = 1.007276466621
WATER = 18.010564684
RESIDUES = {a: float(mass.std_aa_mass[a]) for a in "ACDEFGHIKLMNPQRSTVWY"}


def digest(sequence, missed=0):
    """Return zero-based half-open coordinates and peptides in starting order."""
    if missed < 0:
        raise ValueError("missed must be nonnegative")
    bounds = [0] + [
        i + 1
        for i, a in enumerate(sequence)
        if a in "KR" and (i + 1 == len(sequence) or sequence[i + 1] != "P")
    ]
    if bounds[-1] != len(sequence):
        bounds.append(len(sequence))
    return [
        (start, end, sequence[start:end])
        for i, start in enumerate(bounds[:-1])
        for end in bounds[i + 1 : i + missed + 2]
    ]


def fragments(peptide):
    """Singly charged b/y ions, indexed by ion series and fragment length."""
    residues = np.array([RESIDUES[a] for a in peptide])
    return (
        np.cumsum(residues)[:-1] + PROTON,
        np.cumsum(residues[::-1])[:-1] + WATER + PROTON,
    )


def gaussian(x, centre, width):
    return np.exp(-0.5 * ((x - centre) / width) ** 2)


def qvalues(score, decoy):
    """One winning PSM per spectrum, equally sized target and decoy databases."""
    s = np.asarray(score)
    decoy = np.asarray(decoy, dtype=bool)
    cutoffs = np.unique(s)[::-1]
    fdr = []
    for threshold in cutoffs:
        keep = s >= threshold
        nt = np.sum(keep & ~decoy)
        fdr.append(min(1.0, (np.sum(keep & decoy) + 1) / nt) if nt else 1.0)
    q = np.minimum.accumulate(fdr[::-1])[::-1]
    return cutoffs, np.array(fdr), q


def parsimony(mapping, observed):
    names = sorted(mapping)
    for k in range(len(names) + 1):
        answers = [
            group
            for group in combinations(names, k)
            if observed <= set().union(*(mapping[p] for p in group))
        ]
        if answers:
            return answers
    return []


def maxlfq(logs):
    """Solve the median log-ratio equations for one connected sample group."""
    logs = np.asarray(logs, dtype=float)
    n = logs.shape[1]
    design, ratios = [], []
    for i, j in combinations(range(n), 2):
        keep = np.isfinite(logs[:, i]) & np.isfinite(logs[:, j])
        if keep.any():
            row = np.zeros(n)
            row[j] = 1.0
            row[i] = -1.0
            design.append(row)
            ratios.append(np.median(logs[keep, j] - logs[keep, i]))
    if n > 1 and (not design or np.linalg.matrix_rank(np.array(design)) != n - 1):
        raise ValueError("Samples form disconnected components")
    # Choose the zero-mean solution. Only relative log abundance is identifiable.
    design.append(np.ones(n))
    ratios.append(0.0)
    return np.linalg.lstsq(design, ratios, rcond=None)[0]


def kabsch(moving, fixed):
    source = moving - moving.mean(axis=0)
    target = fixed - fixed.mean(axis=0)
    u, _, vt = np.linalg.svd(source.T @ target)
    sign = np.ones(3)
    sign[-1] = np.sign(np.linalg.det(u @ vt))
    rotation = (u * sign) @ vt
    return source @ rotation + fixed.mean(axis=0), rotation
