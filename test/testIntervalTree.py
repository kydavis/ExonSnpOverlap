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


if	__name__ == '__main__':
	unittest.main()
