"""Numerical and combinatorial checks for edge cases in the teaching algorithms."""

import itertools
import sys
import unittest
from pathlib import Path
import numpy as np
import edlib

subjects = Path(__file__).resolve().parent / "Computational Biology"
sys.path.insert(0, str(subjects / "Computational Genomics"))
sys.path.insert(0, str(subjects / "Computational Proteomics"))
from genome_methods import bit_distance, dp_align, gotoh, hirschberg, wavefront
from peptide_methods import digest, fragments, kabsch, maxlfq, parsimony, qvalues


class AlignmentChecks(unittest.TestCase):
    def test_short_pairs_including_empty_inputs(self):
        words = [
            "".join(v) for n in range(5) for v in itertools.product("AC", repeat=n)
        ]
        for left, right in itertools.product(words, repeat=2):
            with self.subTest(left=left, right=right):
                self.assertEqual(wavefront(left, right)[0], gotoh(left, right)[0])
                self.assertEqual(
                    bit_distance(left, right), edlib.align(left, right)["editDistance"]
                )
                a, b = hirschberg(left, right)
                self.assertEqual(a.replace("-", ""), left)
                self.assertEqual(b.replace("-", ""), right)
                score = sum(
                    -2 if "-" in (x, y) else 2 if x == y else -1 for x, y in zip(a, b)
                )
                self.assertEqual(score, dp_align(left, right)[0])


class PeptideChecks(unittest.TestCase):
    def test_digestion_and_empty_sets(self):
        self.assertEqual(digest(""), [])
        self.assertEqual(digest("AKPGR"), [(0, 5, "AKPGR")])
        self.assertEqual(parsimony({"p": {"a"}}, set()), [()])
        self.assertEqual(parsimony({"p": {"a"}}, {"b"}), [])
        self.assertEqual(fragments("A")[0].size, 0)

    def test_tied_scores_and_relative_abundance(self):
        s, f, q = qvalues([8, 8, 7, 5], [0, 1, 0, 0])
        np.testing.assert_array_equal(s, [8, 7, 5])
        np.testing.assert_allclose(f, [1, 1, 2 / 3])
        np.testing.assert_allclose(q, [2 / 3, 2 / 3, 2 / 3])
        with self.assertRaises(ValueError):
            maxlfq([[4, np.nan], [np.nan, 6]])
        np.testing.assert_allclose(maxlfq([[10.0, 12.0], [5.0, 7.0]]), [-1, 1])

    def test_rotation_excludes_reflections(self):
        p = np.array(
            [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
        )
        aligned, r = kabsch(p * np.array([-1, 1, 1]), p)
        self.assertGreater(np.linalg.det(r), 0.0)
        self.assertGreater(np.linalg.norm(aligned - p), 0.1)


if __name__ == "__main__":
    unittest.main()
