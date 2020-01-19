"""
Given that integers are being read from a data stream. Find median of all the elements read so far starting from the
first integer till the last integer. This is also called Median of Running Integers.
 The data stream can be any source of data, example: a file, an array of integers, input stream etc.

What is Median?

Median can be defined as the element in the data set which separates the higher half of the data sample from the
lower half. In other words we can get the median element as, when the input size is odd, we take the middle
element of sorted data. If the input size is even, we pick average of middle two elements in sorted stream.
"""
import heapq


class MedianFinderSort:
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.data = []

	def addNum(self, num):
		self.data.append(num)

	def findMedian(self):
		self.data.sort()
		if len(self.data) == 0: return 0
		if len(self.data) % 2 == 1:
			return self.data[len(self.data) // 2]
		return (self.data[len(self.data) // 2] + self.data[len(self.data) // 2 - 1]) / float(2)


class MedianFinderHeap(object):
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.minheap = []
		self.maxheap = []

	def addNum(self, num):
		"""
		:type num: int
		:rtype: None
		"""
		if len(self.maxheap) == 0 or num < -self.maxheap[0]:
			heapq.heappush(self.maxheap, -num)
		else:
			heapq.heappush(self.minheap, num)

		l1 = len(self.maxheap)
		l2 = len(self.minheap)
		if l1 - l2 > 1:
			top = heapq.heappop(self.maxheap)
			heapq.heappush(self.minheap, -top)
		elif l2 - l1 > 1:
			top = heapq.heappop(self.minheap)
			heapq.heappush(self.maxheap, -top)

	def findMedian(self):
		"""
		:rtype: float
		"""
		l1 = len(self.maxheap)
		l2 = len(self.minheap)
		total_length = l1 + l2
		if total_length % 2 == 0:
			top1 = -self.maxheap[0]
			top2 = self.minheap[0]
			return (top1 + top2) / 2.0
		else:
			if l1 > l2:
				return -self.maxheap[0]
			else:
				return self.minheap[0]


if __name__ == "__main__":
	m = MedianFinderSort()
	m.addNum(5)
	print m.findMedian()
	m.addNum(15)
	print m.findMedian()
	m.addNum(10)
	print m.findMedian()
	m.addNum(20)
	print m.findMedian()
	m.addNum(3)
	print m.findMedian()

	print "\nUsing Heap method\n"
	m_h = MedianFinderHeap()
	m_h.addNum(5)
	print m_h.findMedian()
	m_h.addNum(15)
	print m_h.findMedian()
	m_h.addNum(10)
	print m_h.findMedian()
	m_h.addNum(20)
	print m_h.findMedian()
	m_h.addNum(3)
	print m_h.findMedian()