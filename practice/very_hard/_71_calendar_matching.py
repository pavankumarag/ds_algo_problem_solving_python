"""
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double
booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open
interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common
to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without
causing a double booking. Otherwise, return false and do not add the event to the calendar.

Example:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.

Reference: https://leetcode.com/problems/my-calendar-i
"""


class MyCalendar: # Bruteforce, Takes O(n2) time and O(n) space
	def __init__(self):
		self.calendar = []

	def book(self, start, end):
		for s,e in self.calendar:
			if s < end and start < e:
				return False
		self.calendar.append([start, end])
		return True

class Node:
	__slots__ = 'start', 'end', 'left', 'right'
	def __init__(self, start, end):
		self.start = start
		self.end = end
		self.left = None
		self.right = None

	def insert(self, node):
		if node.start >= self.end:
			if self.right is None:
				self.right = node
				return True
			self.right.insert(node)
		elif node.end <= self.start:
			if self.left is None:
				self.left = node
				return True
			self.left.insert(node)
		else:
			return False


'''
O(n2) worst case, with O(N \log N)O(NlogN) on random data. For each new event, we insert the event into our binary tree. 
 As this tree may not be balanced, it may take a linear number of steps to add each event.

O(n) space
'''
class MyCalendarOptimised:
	def __init__(self):
		self.root = None

	def book(self, start, end):
		if self.root is None:
			self.root = Node(start, end)
			return True
		return self.root.insert(Node(start, end))


if __name__ == "__main__":
	cal = MyCalendar()
	print cal.book(10, 20)
	print cal.book(15,25)
	print cal.book(20,30)
	cal_o = MyCalendarOptimised()
	print cal_o.book(10, 20)
	print cal_o.book(15, 25)
	print cal_o.book(20, 30)