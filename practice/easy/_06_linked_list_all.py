class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_at_end(self, data):
		new_node = Node(data)
		temp = self.head
		while temp.next is not None:
			temp = temp.next
		temp.next = new_node
		new_node.next = None

	def insert_at_position(self, data, k):
		new_node = Node(data)
		temp = self.head
		count = 1
		while count < k - 1:
			temp = temp.next
			count += 1
		print temp.data
		save = temp.next
		temp.next = new_node
		new_node.next = save

	def delete_at_beginning(self):
		print "Node deleted is ", self.head.data
		self.head = self.head.next

	def delete_at_end(self):
		prev = None
		cur = self.head
		while cur.next is not None:
			prev = cur
			cur = cur.next
		print "Node deleted is ", cur.data
		prev.next = None

	def delete_at_position(self, k):
		# can avoid using two space : prev and cur, using below logic
		if k > 1:
			temp = self.head
			count = 1
			while count < k - 1:
				temp = temp.next
				count += 1
			print "Node deleted is ", temp.next.data
			temp.next = temp.next.next
		elif k == 1:
			print "Node deleted is ", self.head.data
			self.head = self.head.next
		else:
			print "Please enter valid position"
			return -1

	def print_from_beginning(self, node):
		if node is None:
			print
			return
		print node.data,
		self.print_from_beginning(node.next)

	def print_from_end(self, node):
		if node is None:
			print
			return
		self.print_from_end(node.next)
		print node.data,

	def reverse_brute_force(self):
		prev = None
		cur = self.head
		while cur.next is not None:
			next_n = cur.next
			cur.next = prev
			prev = cur
			cur = next_n
		self.head = cur
		cur.next = prev

	def reverse_bf_recursive(self, prev, cur):
		if cur.next is None:
			self.head = cur
			cur.next = prev
			return
		next_n = cur.next
		cur.next = prev
		prev = cur
		cur = next_n
		self.reverse_bf_recursive(prev, cur )

	def reverse_recursive(self, cur):
		if cur.next is None:
			self.head = cur
			return
		self.reverse_recursive(cur.next)
		next_n = cur.next
		next_n.next = cur
		cur.next = None


if __name__ == "__main__":
	l = LinkedList()
	l.insert_at_beginning(2)
	l.insert_at_beginning(4)
	l.insert_at_beginning(6)
	l.insert_at_beginning(7)
	l.print_from_beginning(l.head)
	l.insert_at_end(8)
	l.insert_at_end(10)
	l.print_from_beginning(l.head)
	l.print_from_end(l.head)
	l.delete_at_beginning()
	l.delete_at_end()
	l.print_from_beginning(l.head)
	#print l.head.data
	l.insert_at_position(11, 2)
	l.print_from_beginning(l.head)
	l.delete_at_position(2)
	l.print_from_beginning(l.head)
	l.reverse_brute_force()
	l.print_from_beginning(l.head)
	l.reverse_bf_recursive(None, l.head)
	l.print_from_beginning(l.head)
	l.reverse_recursive(l.head)
	l.print_from_beginning(l.head)

