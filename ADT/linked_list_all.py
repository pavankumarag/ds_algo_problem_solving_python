class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def reverse(self):
		prev = None
		cur = self.head
		while cur is not None:
			next = cur.next
			cur.next = prev
			prev = cur
			cur = next
		self.head = prev

	def reverse_util(self, cur, prev):
		if cur.next is None:
			self.head = cur
			cur.next = prev
			return
		next = cur.next
		cur.next = prev
		self.reverse_util(next, cur)

	def reverse_recursive_from_iterative(self):  # converting iterative to recursive
		if self.head is None:
			return
		self.reverse_util(self.head, None)

	def reverse_recursive(self, p):
		if p.next is None:
			self.head = p
			return
		self.reverse_recursive(p.next)
		q = p.next
		q.next = p
		p.next = None

	# insert new node at the beginning
	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def print_list(self):
		temp = self.head
		while (temp):
			print temp.data,
			temp = temp.next

	def print_recursive(self, node):
		if node is None:
			print
			return
		print node.data,
		self.print_recursive(node.next)

	def print_end_recursive(self, node):
		if node is None:
			print
			return
		self.print_end_recursive(node.next)
		print node.data,


if __name__ == "__main__":
	l = LinkedList()
	l.push(10)
	l.push(12)
	l.push(2)
	l.push(3)
	l.push(5)
	l.print_list()
	l.reverse()
	print "\nReversing the linked list\n"
	l.print_list()
	print "\nReversing the linked list using recursion built from iterative method\n"
	l.reverse_recursive_from_iterative()
	l.print_list()
	print "\nReversing the linked list using direct recursion\n"
	l.reverse_recursive(l.head)
	l.print_list()
	print "\nPrinting from Beginning using recursion\n"
	l.print_recursive(l.head)
	print "\nPrinting from the end using recursion"
	l.print_end_recursive(l.head)


