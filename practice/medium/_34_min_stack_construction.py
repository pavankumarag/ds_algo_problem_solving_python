"""
Min Max stack construction


Design a Data Structure SpecialStack that supports all the stack operations
like push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should return minimum element
from the SpecialStack. All these operations of SpecialStack must be O(1).
To implement SpecialStack, you should only use standard Stack data structure and no other data structure like
arrays, list, .. etc.
https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
"""
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:
	def __init__(self):
		self.top = None
		self.count = 0
		self.min = None

	def display(self):
		temp = self.top
		out = []
		while temp is not None:
			out.append(temp.data)
			temp = temp.next
		#out = "\n".join(out)
		return out

	def push(self, value):
		if self.top is None:
			self.top = Node(value)
			self.min = value
		elif value < self.min:
			temp = 2*value - self.min
			new_node = Node(temp)
			new_node.next = self.top
			self.top = new_node
			self.min = value
		else:
			new_node = Node(value)
			new_node.next = self.top
			self.top = new_node
		print("Number Inserted: {}".format(value))

	def pop(self):
		if self.top is None:
			print "stack is empty"
			return -1
		else:
			removed_node = self.top
			self.top = self.top.next
			if removed_node.data < self.min:
				print "top most ele removed", self.min
				self.min = 2*self.min - removed_node.data
			else:
				print "top most ele removed", removed_node.data

	def peek(self):
		if self.top is None:
			print "stack is empty"
			return -1
		elif self.top.data < self.min:
			print "Top most ele", self.min
		else:
			print "Top most ele", self.top.data

	def get_min(self):
		if self.top is None:
			print "stack is empty"
			return -1
		else:
			print "Min ele", self.min


if __name__ == "__main__":
	s = Stack()
	s.push(3)
	s.push(5)
	print s.display()
	s.get_min()
	s.push(2)
	s.push(1)
	print s.display()
	s.get_min()
	s.pop()
	print s.display()
	s.peek()
	s.get_min()