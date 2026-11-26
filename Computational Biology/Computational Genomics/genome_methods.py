"""Small reference implementations for the genomics lectures.

Global and local alignment: https://doi.org/10.1016/0022-2836(70)90057-4
Smith and Waterman: https://doi.org/10.1016/0022-2836(81)90087-5
Affine gaps: https://doi.org/10.1016/0022-2836(82)90398-9
Wavefront alignment: https://doi.org/10.1093/bioinformatics/btaa777
"""

from collections import Counter, defaultdict
from itertools import product
import numpy as np
import matplotlib.pyplot as plt


def dp_align(a, b, local=False, match=2, mismatch=-1, gap=-2):
    n, m = len(a), len(b)
    score = np.zeros((n + 1, m + 1), int)
    move = np.zeros_like(score)
    if not local:
        score[:, 0] = np.arange(n + 1) * gap
        score[0, :] = np.arange(m + 1) * gap
        move[1:, 0] = 2
        move[0, 1:] = 3
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            values = [
                score[i - 1, j - 1] + (match if a[i - 1] == b[j - 1] else mismatch),
                score[i - 1, j] + gap,
                score[i, j - 1] + gap,
            ]
            k = int(np.argmax(values))
            best = values[k]
            if not local or best > 0:
                score[i, j] = best
                move[i, j] = k + 1
    i, j = np.unravel_index(score.argmax(), score.shape) if local else (n, m)
    value = int(score[i, j])
    path = [(i, j)]
    u = []
    v = []
    while move[i, j]:
        k = move[i, j]
        u.append(a[i - 1] if k != 3 else "-")
        v.append(b[j - 1] if k != 2 else "-")
        i -= int(k != 3)
        j -= int(k != 2)
        path.append((i, j))
    return value, "".join(reversed(u)), "".join(reversed(v)), score, path[::-1]


def show_dp(a, b, matrix, path):
    fig, ax = plt.subplots(figsize=(6.4, 3.7), constrained_layout=True)
    im = ax.imshow(matrix, cmap="viridis", aspect="auto")
    i, j = np.array(path).T
    ax.plot(j, i, "o-", ms=3, color="#fe9563")
    ax.set(
        xticks=range(len(b) + 1),
        xticklabels=["∅", *b],
        yticks=range(len(a) + 1),
        yticklabels=["∅", *a],
        xlabel="Sequence B prefix",
        ylabel="Sequence A prefix",
        title="Dynamic programme and traceback",
    )
    fig.colorbar(im, ax=ax, label="Score")


def last_row(a, b):
    prev = np.arange(len(b) + 1) * -2
    for char in a:
        row = np.empty_like(prev)
        row[0] = prev[0] - 2
        for j, c in enumerate(b, 1):
            row[j] = max(
                prev[j - 1] + (2 if char == c else -1), prev[j] - 2, row[j - 1] - 2
            )
        prev = row
    return prev


def hirschberg(a, b):
    if not a:
        return "-" * len(b), b
    if not b:
        return a, "-" * len(a)
    if min(len(a), len(b)) <= 1:
        return dp_align(a, b)[1:3]
    mid = len(a) // 2
    forward = last_row(a[:mid], b)
    back = last_row(a[mid:][::-1], b[::-1])[::-1]
    split = int(np.argmax(forward + back))
    del forward, back
    l, r = hirschberg(a[:mid], b[:split])
    u, v = hirschberg(a[mid:], b[split:])
    return l + u, r + v


def gotoh(a, b, mis=2, opening=3, extension=1):
    n, m = len(a), len(b)
    h = np.full((n + 1, m + 1), np.inf)
    d = h.copy()
    ins = h.copy()
    h[0, 0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if i == j == 0:
                continue
            if i:
                d[i, j] = min(
                    h[i - 1, j] + opening + extension, d[i - 1, j] + extension
                )
            if j:
                ins[i, j] = min(
                    h[i, j - 1] + opening + extension, ins[i, j - 1] + extension
                )
            diagonal = (
                h[i - 1, j - 1] + mis * (a[i - 1] != b[j - 1]) if i and j else np.inf
            )
            h[i, j] = min(diagonal, d[i, j], ins[i, j])
    return int(h[-1, -1]), h, d, ins


def wavefront(a, b, mis=2, opening=3, extension=1):
    """Furthest row reached on each diagonal k=i-j, indexed by integer cost."""
    if min(mis, extension) < 1 or opening < 0:
        raise ValueError("Integer penalties need positive mismatch and extension")
    M = {}
    D = {}
    I = {}
    n, m = len(a), len(b)
    profile = []

    def take(table, s, k, di, dj):
        i = table.get((s, k))
        if i is None:
            return -1
        j = i - k
        return i + di if i + di <= n and j + dj <= m else -1

    cap = mis * min(n, m) + (opening + abs(n - m) * extension if n != m else 0)
    for cost in range(cap + 1):
        active = 0
        for k in range(-min(m, cost // extension), min(n, cost // extension) + 1):
            down = max(
                take(M, cost - opening - extension, k - 1, 1, 0),
                take(D, cost - extension, k - 1, 1, 0),
            )
            across = max(
                take(M, cost - opening - extension, k + 1, 0, 1),
                take(I, cost - extension, k + 1, 0, 1),
            )
            if down >= 0:
                D[cost, k] = down
            if across >= 0:
                I[cost, k] = across
            i = max(
                down, across, take(M, cost - mis, k, 1, 1), 0 if cost == k == 0 else -1
            )
            if i < 0:
                continue
            j = i - k
            while i < n and j < m and a[i] == b[j]:
                i += 1
                j += 1
            M[cost, k] = i
            active += 1
        profile.append(active)
        if M.get((cost, n - m)) == n:
            return cost, profile
    raise RuntimeError("A valid upper bound was exhausted")


def bit_distance(pattern, text):
    """Myers' global edit score; Python integers supply the bit vector."""
    if not pattern:
        return len(text)
    full = (1 << len(pattern)) - 1
    high = 1 << (len(pattern) - 1)
    positive = full
    negative = 0
    score = len(pattern)
    masks = defaultdict(int)
    for j, c in enumerate(pattern):
        masks[c] |= 1 << j
    for c in text:
        eq = masks[c]
        xv = eq | negative
        xh = (((eq & positive) + positive) ^ positive) | eq
        ph = negative | ~(xh | positive)
        mh = positive & xh
        score += int(bool(ph & high)) - int(bool(mh & high))
        ph = ((ph << 1) | 1) & full
        mh = (mh << 1) & full
        positive = (mh | ~(xv | ph)) & full
        negative = ph & xv
    return score


def rc(s):
    return s.translate(str.maketrans("ACGT", "TGCA"))[::-1]


def kmers(s, k):
    if k < 1:
        raise ValueError("k must be positive")
    return [s[i : i + k] for i in range(len(s) - k + 1)]


def canon(k):
    return min(k, rc(k))


def minimisers(s, k, w):
    if w < 1:
        raise ValueError("Window needs at least one k-mer")
    keys = [canon(kmer) for kmer in kmers(s, k)]
    selected = []
    for i in range(len(keys) - w + 1):
        j = min(range(i, i + w), key=lambda n: (keys[n], -n))
        if not selected or selected[-1] != j:
            selected.append(j)
    return selected, keys


def fm_index(s):
    if "$" in s or any(c <= "$" for c in s):
        raise ValueError("Use an alphabet above the unique sentinel")
    text = s + "$"
    sa = sorted(range(len(text)), key=lambda i: text[i:])
    last = "".join(text[i - 1] for i in sa)
    alphabet = sorted(set(last))
    C = {}
    total = 0
    for c in alphabet:
        C[c] = total
        total += last.count(c)
    occ = {c: np.r_[0, np.cumsum([v == c for v in last])] for c in alphabet}
    return sa, last, C, occ


def backward(query, index):
    if "$" in query:
        raise ValueError("The sentinel is reserved")
    sa, last, C, occ = index
    lo, hi = 0, len(sa)
    widths = [hi]
    for c in reversed(query):
        if c not in C:
            lo = hi = 0
        else:
            lo, hi = C[c] + int(occ[c][lo]), C[c] + int(occ[c][hi])
        widths.append(hi - lo)
    return sorted(sa[lo:hi]), widths


def euler_spelling(s, k):
    if not 2 <= k <= len(s):
        raise ValueError("Choose k between two and sequence length")
    graph = defaultdict(list)
    balance = Counter()
    for word in kmers(s, k):
        u, v = word[:-1], word[1:]
        graph[u].append(v)
        balance[u] += 1
        balance[v] -= 1
    start = next((u for u, d in balance.items() if d == 1), s[: k - 1])
    for neighbours in graph.values():
        neighbours.sort(reverse=True)
    path = []
    stack = [start]
    while stack:
        u = stack[-1]
        if graph[u]:
            stack.append(graph[u].pop())
        else:
            path.append(stack.pop())
    path = path[::-1]
    return path[0] + "".join(x[-1] for x in path[1:]), path


def rng_dna(rng, n):
    return "".join(rng.choice(list("ACGT"), size=n))


def bars(labels, values, title, ylabel):
    fig, ax = plt.subplots(figsize=(6.1, 3.1), constrained_layout=True)
    ax.bar(labels, values, color="#36768b")
    ax.set(ylabel=ylabel, title=title)
