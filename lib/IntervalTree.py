
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
			interval with one or two points

		Return:
			List of intervals in tree that overlap
	"""
	def querey(interval):
		ret = set()
		if (len(interval) == 1 or interval[0] == interval[1]):
			self._quereyPoint(interval[0], ret)
		elif (len(interval) == 2):
			self._quereyRange(interval, ret)
		else:
			raise ValueError("Interval Tree Querey takes a list of a maximum of two values ie. ([1] or [1, 2])")
		return (ret)

	def _quereyPoint(point, ret):
		left = self.left
		right = self.right
		while (left and right)
		return (ret)

	def _quereyRange(interval, ret):
		left = self._quereyPoint(interval[0], ret)
		right = self._quereyPoint(interval[1], ret)
		return (ret)
