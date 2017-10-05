import unittest
from lib.Range import Range

class	TestRange(unittest.TestCase):

	def test_overlapOneWay(self):
		rng1 = Range(1, 10)
		rng2 = Range(5, 15)
		self.assertEqual(rng1.overlap(rng2), True)
		self.assertEqual(rng2.overlap(rng1), True)

	def test_overlapEncompass(self):
		rng1 = Range(1, 10)
		rng2 = Range(5, 9)
		self.assertEqual(rng1.overlap(rng2), True)
		self.assertEqual(rng2.overlap(rng1), True)

	def test_overlapEqual(self):
		rng1 = Range(1, 10)
		rng2 = Range(1, 10)
		self.assertEqual(rng1.overlap(rng2), True)
		self.assertEqual(rng2.overlap(rng1), True)

	def test_noOverlap(self):
		rng1 = Range(1, 10)
		rng2 = Range(11, 13)
		self.assertEqual(rng1.overlap(rng2), False)
		self.assertEqual(rng2.overlap(rng1), False)
