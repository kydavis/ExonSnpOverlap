from lib.Range import Range

"""
	Purpose:
		Hold and organize genome data extracted from GFF or BED files

	Structure:
		Dictionary with chromosome/scaffold keys and an array of ranges as the value
"""


class GenomicRanges:

	def __init__(self):
		self.ranges = {}
	
	"""
		Purpose:
			Finds the insertion place for the range in the corresponding chromsome
			Start of the range is the first priority followed by end of the range
	"""
	def _findInsertion(self, chromosome, rng):
		start = 0
		end = len(chromosome)
		while (start < end):
			mid = (start + end) / 2
			if (rng[0] < chromosome[mid][0]):
				end = mid
			elif (rng[0] > chromosome[mid][0]):
				start = mid + 1
			else: 
				if (rng[1] < chromosome[mid][1]):
					end = mid
				elif(rng[1] > chromosome[mid][1]):
					start = mid + 1
				else:
					return (start)
		return (start)


	def addRange(self, chromosome, start, end):
		if (len(chromosome) > 3 and chromosome[:3] == 'chr'):
			chromosome = chromosome[3]
		rng = Range(start, end)
		rng = tuple([min(start, end), max(start, end)])
		if (chromosome in self.ranges):
			insert = self._findInsertion(self.ranges[chromosome], rng)
			self.ranges[chromosome].insert(insert, rng)
		else:
			self.ranges[chromosome] = [rng]
