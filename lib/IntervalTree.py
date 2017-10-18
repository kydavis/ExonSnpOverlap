
class IntervalTree:

	class	ITNode:

		"""
			Class attributes:
				mid: Center of the largest range
				left: Subtree containing intervals completely left of center
				right: Subtree containing intervals completely right of center
				startOverlap: List of overlapping ranges sorted by start point
				endOverlap: List of overlapping ranges sorted by end point
		"""

		"""
			Init parameters:
		"""

		def __init__(self, mid):
			self.mid = mid
			self.left = None
			self.right = None
			self.overlap = None
			self.overlapStart = None
			self.overlapEnd = None
			

	"""
		Init parameters:
			Intervals: List of interval tuples SORTED BY FIRST VALUE IN THE TUPLE for the construction of the tree.
	"""
	def __init__(self, intervals):
		self.mid = intervals[(len(intervals) - 1) / 2][0]
		self.left = None
		self.right = None
		leftIntervals = []
		midIntervals = []
		rightIntervals = []
		for interval in intervals:
			if (interval[1] < self.mid):
				leftIntervals.append(interval)
			elif (interval[0] > self.mid):
				rightIntervals.append(interval)
			else:
				midIntervals.append(interval)
		self.overlapStart = list(midIntervals)
		midIntervals.sort(key=lambda x: x[1], reverse=True)
		self.overlapEnd = midIntervals
		if (len(leftIntervals) > 0):
			self.left = IntervalTree(leftIntervals)
		if (len(rightIntervals) > 0):
			self.right = IntervalTree(rightIntervals)

	def __repr__(self):
		return("""
Mid:{}
Sorted Start:{}
Sorted End:{}

Left:
	{}

Right:
	{}
""".format(self.mid, self.overlapStart, self.overlapEnd, self.left, self.right))


	"""
		Purpose:
			Find all intervals in tree that the input interval overlaps with

		Parameters:
			start: Start of query interval
			end: End of query interval 

		Return:
			List of intervals in tree that overlap
	"""
	def findOverlap(start, end):
		return (True)
