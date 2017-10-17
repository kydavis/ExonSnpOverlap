import unittest
from lib.GeneData import GenomicIntervals

class	TestGenomicIntervalsMethods(unittest.TestCase):

	def	test_addSingleForward(self):
		test = GenomicIntervals()
		test.addInterval("1", 10, 30)
		self.assertEqual(test.intervals["1"][0][0], 10)
		self.assertEqual(test.intervals["1"][0][1], 30)

	def	test_addSingleReverse(self):
		test = GenomicIntervals()
		test.addInterval("1", 30, 10)
		self.assertEqual(test.intervals["1"][0][0], 10)
		self.assertEqual(test.intervals["1"][0][1], 30)

	def test_addChrPefix(self):
		test = GenomicIntervals()
		test.addInterval("chr1", 10, 30)
		self.assertEqual(test.intervals["1"][0][0], 10)
		self.assertEqual(test.intervals["1"][0][1], 30)

	def test_addMultipleChromosomes(self):
		test = GenomicIntervals()
		test.addInterval("1", 10, 30)
		test.addInterval("2", 5, 7)
		self.assertEqual(test.intervals["2"][0][0],5)
		self.assertEqual(test.intervals["2"][0][1], 7)
		self.assertEqual(test.intervals["1"][0][0],10)
		self.assertEqual(test.intervals["1"][0][1], 30)

	def test_addMultipleIntervals(self):
		test = GenomicIntervals()
		test.addInterval("1", 10, 30)
		test.addInterval("1", 5, 7)
		self.assertEqual(test.intervals["1"][0][0],5)
		self.assertEqual(test.intervals["1"][0][1], 7)
		self.assertEqual(test.intervals["1"][1][0],10)
		self.assertEqual(test.intervals["1"][1][1], 30)

	def test_addEqualStarts(self):
		test = GenomicIntervals()
		test.addInterval("1", 10, 30)
		test.addInterval("1", 10, 15)
		self.assertEqual(test.intervals["1"][0][0],10)
		self.assertEqual(test.intervals["1"][0][1], 15)
		self.assertEqual(test.intervals["1"][1][0],10)
		self.assertEqual(test.intervals["1"][1][1], 30)

	def test_addEqualEnds(self):
		test = GenomicIntervals()
		test.addInterval("1", 10, 30)
		test.addInterval("1", 9, 30)
		self.assertEqual(test.intervals["1"][0][0],9)
		self.assertEqual(test.intervals["1"][0][1], 30)
		self.assertEqual(test.intervals["1"][1][0],10)
		self.assertEqual(test.intervals["1"][1][1], 30)

	def test_addEncompassing(self):
		test = GenomicIntervals()
		test.addInterval("1", 10, 30)
		test.addInterval("1", 11, 29)
		self.assertEqual(test.intervals["1"][0][0],10)
		self.assertEqual(test.intervals["1"][0][1], 30)
		self.assertEqual(test.intervals["1"][1][0],11)
		self.assertEqual(test.intervals["1"][1][1], 29)


if	__name__ == '__main__':
	unittest.main()
