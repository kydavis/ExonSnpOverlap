
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
			Intervals: List of interval tuples for the construction of the tree.
	"""
	def __init__(self, intervals):


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
