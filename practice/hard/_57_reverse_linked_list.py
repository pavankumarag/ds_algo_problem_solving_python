class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def print_l(self):
		temp = self.head
		while temp is not None:
			print temp.data,
			temp = temp.next

	def reverse_iterative(self):
		cur = self.head
		prev = None
		while cur.next != None:
			temp = cur.next
			cur.next = prev
			prev = cur
			cur = temp
		self.head = cur
		cur.next = prev

	def reverse_recursive_from_iterative(self, cur, prev):
		if cur.next is None:
			self.head = cur
			cur.next = prev
			return
		temp = cur.next
		cur.next = prev
		prev = cur
		cur = temp
		self.reverse_recursive_from_iterative(cur, prev)

	def reverse_recursive(self, cur):
		if cur.next is None:
			self.head = cur
			return
		self.reverse_recursive(cur.next)
		next = cur.next
		next.next = cur
		cur.next = None


if __name__ == "__main__":
	l = LinkedList()
	l.head = Node(2)
	l.head.next = Node(3)
	l.head.next.next = Node(4)
	l.head.next.next.next = Node(5)
	l.head.next.next.next.next = Node(1)
	l.print_l()
	l.reverse_iterative()
	print
	l.print_l()
	l.reverse_recursive_from_iterative(l.head, None)
	print
	l.print_l()
	l.reverse_recursive(l.head)
	print
	l.print_l()