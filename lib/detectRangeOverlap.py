
from lib.GeneData import GenomicRanges

"""
	Purpose:
		detectRangeOverlap takes in two list of sorted ranges and returns a list
		of ranges that overlap between the two lists.

	Eg:
		r1:[(10, 30), (10, 33), (13, 28), (14, 15)]

		r2:[(11, 31), (12, 33), (15, 15), (16, 19)]
		output:[{(10, 30) : [(11, 31), (12, 33), (15, 15), (16, 19)]},
				{(10, 33) : [(11, 31), (12, 33), (15, 15), (16, 19)]},
				{(13, 28) : [(11, 31), (12, 33), (15, 15), (16, 19)]},
				{(14, 15) : [(11, 31), (12, 33), (15, 15)]}]
"""
def	detectRangeOverlap(r1, r2):

