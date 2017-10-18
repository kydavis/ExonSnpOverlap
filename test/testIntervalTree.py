import unittest
from lib.IntervalTree import IntervalTree

class	TestIntervalTreeMethods(unittest.TestCase):

	def	test_constructIntervalTree(self):
		test = IntervalTree([(1, 3), (1, 13), (4, 15), (5, 6), (16, 19)])
		self.assertEqual(test.mid, 4)
		self.assertEqual(test.overlapStart[0], (1, 13))
		self.assertEqual(test.overlapEnd[0], (4, 15))
		self.assertEqual(test.left.mid, 1)
		self.assertEqual(test.right.mid, 5)
		self.assertEqual(test.right.right.mid, 16)

	def test_searchPoint(self):
		test = IntervalTree([(1, 3), (1, 13), (4, 15), (5, 6), (16, 19)])
		ret = test.querey([5])
		self.assertEqual(ret, {(5, 6), (1, 13), (4, 15)})
		self.assertEqual(test.querey([1, 1]), {(1, 13), (1, 3)})
		self.assertEqual(test.querey([20]), set())

	def test_searchRange(self):
		test = IntervalTree([(1, 3), (1, 13), (4, 15), (5, 6), (16, 19)])
		self.assertEqual(test.querey([1, 2]), set([(1, 13), (1, 3)]))
		self.assertEqual(test.querey([0, 20]), set([(5, 6), (1, 13), (4, 15), (1, 3), (16, 19)]))
		self.assertEqual(test.querey([20, 25]), set())

if	__name__ == '__main__':
	unittest.main()
