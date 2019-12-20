#-*- coding: utf-8 -*-
'''
Check whether a given Linked List contains loop and if loop is present then removes the loop and returns true.
If the list doesn’t contain loop then it returns false.

Eg: 1->2->3->4->5->2  loop detect
remove 1->2->3->4->5->NULL
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def print_list(self):
		temp = self.head
		while (temp):
			print temp.data,
			temp = temp.next

	def detect_loop(self):
		slow_p, fast_p = self.head, self.head
		while slow_p and fast_p and fast_p.next:
			slow_p = slow_p.next
			fast_p = fast_p.next.next
			if slow_p == fast_p:
				print "Loop detected, removing"
				self.remove_loop(slow_p)
				return True
		return False

	def remove_loop(self, loop_node):
		ptr1, ptr2 = loop_node, loop_node
		k = 1
		while ptr1.next != ptr2:
			ptr1 = ptr1.next
			k += 1

		ptr1 = self.head
		ptr2 = self.head
		for i in range(k):
			ptr2 = ptr2.next

		while ptr1 != ptr2:
			ptr1 = ptr1.next
			ptr2 = ptr2.next

		while ptr2.next != ptr1:
			ptr2 = ptr2.next

		ptr2.next = None


if __name__ == "__main__":
	ll = LinkedList()
	ll.push(1)
	ll.push(2)
	ll.push(3)
	ll.push(4)
	ll.push(5)
	#ll.print_list()
	print ll.head.next.next.next.next.next
	ll.head.next.next.next.next.next = ll.head.next.next
	# ll.print_list()
	print ll.detect_loop()
	#ll.print_list()

	print
	llist = LinkedList()
	llist.head = Node(50)
	llist.head.next = Node(20)
	llist.head.next.next = Node(15)
	llist.head.next.next.next = Node(4)
	llist.head.next.next.next.next = Node(10)
	llist.print_list()
	llist.head.next.next.next.next.next = llist.head.next.next

	llist.detect_loop()

	print "Linked List after removing loop"
	llist.print_list()

