
class IntervalTree:

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
	def querey(self, interval):
		ret = set()
		if (len(interval) == 1 or interval[0] == interval[1]):
			self._quereyPoint(interval[0], ret)
		elif (len(interval) == 2 and interval[0] < interval[1]):
			self._quereyRange(interval, ret)
		else:
			raise ValueError("Interval Tree Querey takes a list of a maximum of two" +
				"values ie. ([1] or [1, 2]) with the first value being less than or" +
				"equal to the second value")
		return (ret)


	"""
		Functions used for searching for a single point within
			the Interval Tree
	"""
	def _addIntervalsPoint(self, point, intervals, ret):
		for interval in intervals:
			if (point >= interval[0] and point <= interval[1]):
				ret.add(interval)
			else:
				return

	def _quereyPoint(self, point, ret):
		if (point < self.mid):
			self._addIntervalsPoint(point, self.overlapStart, ret)
			if (self.left):
				self.left._quereyPoint(point, ret)
		else:
			self._addIntervalsPoint(point, self.overlapEnd, ret)
			if (self.right):
				self.right._quereyPoint(point, ret)

	"""
		Functions used for searching for an interval overlap
			within the Interval Tree
	"""
	
	def _addIntervals(self, value, intervals, ret):
		for interval in intervals:
			if (max(value[0], interval[0]) <= min(value[1], interval[1])):
				ret.add(interval)
			else:
				return

	def _quereyRange(self, value, ret):
		if (value[0] <= self.mid):
			self._addIntervals(value, self.overlapStart, ret)
			if (self.left):
				self.left._quereyRange(value, ret)
			if (value[1] > self.mid and self.right):
				self.right._quereyRange(value, ret)
		else:
			self._addIntervals(value, self.overlapEnd, ret)
			if (self.right):
				self.right._quereyRange(value, ret)
		return
