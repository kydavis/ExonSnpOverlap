
from lib.GeneData import GenomicRanges

"""
	Purpose:
		detectRangeOverlap takes in two list of sorted ranges and returns a list
		of ranges that overlap between the two lists.

"""
"""
	First function takes into account that exons on the same chromosome from the
		same file may overlap.

	Eg:
		r1:[(10, 30), (10, 33), (13, 28), (14, 15)]

		r2:[(11, 31), (12, 33), (15, 15), (16, 19), (32, 33)]
		output:[{(10, 30) : [(11, 31), (12, 33), (15, 15), (16, 19)]},
				{(10, 33) : [(11, 31), (12, 33), (15, 15), (16, 19), (32, 33)]},
				{(13, 28) : [(11, 31), (12, 33), (15, 15), (16, 19)]},
				{(14, 15) : [(11, 31), (12, 33), (15, 15)]}]
"""

"""
def	detectRangeOverlap(r1, r2):
	return (True)
"""

"""
	Second function assumes that exons/SNPs on the same chromosome from the same
		file cannot overlap

	Eg:
		r1:[(10, 30), (32, 33), (49, 50), (55, 79)]

		r2:[(11, 31), (33, 50), (51, 52), (78, 80)]

		output:[{(10, 30) : [(11, 31)]},
				{(32, 33) : [(33, 50)]},
				{(49, 50) : [(33, 50)]},
				{(55, 79) : [(78, 80)]}]

		If overlap and rng1.end > rng2.end then increment rng2, else increment rng1
"""

def detectRangeOverlaps(r1, r2):
	i = 0
	j = 0
	r1_len = len(r1)
	r2_len = len(r2)
	overlaps = {}
	while (i < r1_len and j < r2_len):
		rng1 = r1[i]
		rng2 = r2[j]
		if (rng1.isOverlap(rng2)):
			if (rng1 in overlaps):
				overlaps[rng1.name].append(rng2)
			else:
				overlaps[rng1.name] = [rng2]
		if (rng1.end < rng2.end):
			i += 1
		else:
			j += 1
	return (overlaps)




