
"""
	Purpose:
		Class to hold the start and end point of ranges
"""

class Range:

	"""
		Parameters:
			Start: start of the genomic range
			End: end of the genomic range (inclusive)
	"""
	def __init__(self, x1, x2):
		self.start = min(x1, x2)
		self.end = max(x1, x2)
		self.name = "({}, {})".format(self.start, self.end)

	"""
		Detects if a range overlaps with this range
	"""
	def isOverlap(self, rng2):
		return (max(self.start, rng2.start) <= min(self.end, rng2.end))

	def __repr__(self):
		return ("({}, {})".format(self.start, self.end))
