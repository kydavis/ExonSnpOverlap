import unittest
from lib.detectRangeOverlap import detectRangeOverlaps
from lib.Range import Range

class	TestDetectRangeOverlap(unittest.TestCase):

	def	test_simpleOverlaps(self):
		r1 = [Range(10,30), Range(32, 33), Range(49, 50)]
		r2 = [Range(11,31), Range(33, 34), Range(50, 50)]
		print(detectRangeOverlaps(r1, r2))
		overlaps = detectRangeOverlaps(r1, r2)
		self.assertEqual(overlaps["(10, 30)"][0].start, 11)
		self.assertEqual(overlaps["(32, 33)"][0].start, 33)
		self.assertEqual(overlaps["(49, 50)"][0].start, 50)

#	def	test_simpleOverlaps(self):
#		r1 = [Range(10,30), Range(32, 33), Range(49, 50)]
#		r2 = [Range(11,31), Range(33, 34), Range(50, 50)]
#		print(detectRangeOverlaps(r1, r2))
