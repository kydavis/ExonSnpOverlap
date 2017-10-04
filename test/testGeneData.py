import unittest
from lib.GeneData import GenomicRanges

class	TestGenomicRangesMethods(unittest.TestCase):

	def	test_addSingleForward(self):
		test = GenomicRanges()
		test.addRange("1", 10, 30)
		self.assertEqual(test.ranges["1"][0].start, 10)
		self.assertEqual(test.ranges["1"][0].end, 30)

	def	test_addSingleReverse(self):
		test = GenomicRanges()
		test.addRange("1", 30, 10)
		self.assertEqual(test.ranges["1"][0].start, 10)
		self.assertEqual(test.ranges["1"][0].end, 30)

	def test_addChrPefix(self):
		test = GenomicRanges()
		test.addRange("chr1", 10, 30)
		self.assertEqual(test.ranges["1"][0].start, 10)
		self.assertEqual(test.ranges["1"][0].end, 30)

	def test_addMultipleChromosomes(self):
		test = GenomicRanges()
		test.addRange("1", 10, 30)
		test.addRange("2", 5, 7)
		self.assertEqual(test.ranges["2"][0].start,5)
		self.assertEqual(test.ranges["2"][0].end, 7)
		self.assertEqual(test.ranges["1"][0].start,10)
		self.assertEqual(test.ranges["1"][0].end, 30)

	def test_addMultipleRanges(self):
		test = GenomicRanges()
		test.addRange("1", 10, 30)
		test.addRange("1", 5, 7)
		self.assertEqual(test.ranges["1"][0].start,5)
		self.assertEqual(test.ranges["1"][0].end, 7)
		self.assertEqual(test.ranges["1"][1].start,10)
		self.assertEqual(test.ranges["1"][1].end, 30)

	def test_addEqualStarts(self):
		test = GenomicRanges()
		test.addRange("1", 10, 30)
		test.addRange("1", 10, 15)
		self.assertEqual(test.ranges["1"][0].start,10)
		self.assertEqual(test.ranges["1"][0].end, 15)
		self.assertEqual(test.ranges["1"][1].start,10)
		self.assertEqual(test.ranges["1"][1].end, 30)

	def test_addEqualEnds(self):
		test = GenomicRanges()
		test.addRange("1", 10, 30)
		test.addRange("1", 9, 30)
		self.assertEqual(test.ranges["1"][0].start,9)
		self.assertEqual(test.ranges["1"][0].end, 30)
		self.assertEqual(test.ranges["1"][1].start,10)
		self.assertEqual(test.ranges["1"][1].end, 30)

	def test_addEncompassing(self):
		test = GenomicRanges()
		test.addRange("1", 10, 30)
		test.addRange("1", 11, 29)
		self.assertEqual(test.ranges["1"][0].start,10)
		self.assertEqual(test.ranges["1"][0].end, 30)
		self.assertEqual(test.ranges["1"][1].start,11)
		self.assertEqual(test.ranges["1"][1].end, 29)


if	__name__ == '__main__':
	unittest.main()
