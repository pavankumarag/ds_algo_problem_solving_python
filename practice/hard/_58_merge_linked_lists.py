"""
Merge two sorted linked lists

Write a SortedMerge() function that takes two lists, each of which is sorted in increasing order, and merges the two
together into one list which is in increasing order. SortedMerge() should return the new list.
 The new list should be made by splicing together the nodes of the first two lists.

For example if the first linked list a is 5->10->15 and the other linked list b is 2->3->20,
then SortedMerge() should return a pointer to the head node of the merged list 2->3->5->10->15->20.
"""

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def merged_trail(self, l1, l2):
		if l1.head is None:
			self.head = l2.head
		elif l2.head is None:
			self.head = l1.head
		cur_1 = l1.head
		cur_2 = l2.head
		cur = self.head
		while cur_1 is not None or cur_2 is not None:
			if cur_1.data <= cur_2.data:
				cur = cur_1
				cur_1 = cur_1.next
			else:
				cur = cur_2
				cur_2 = cur_2.next
		if cur_1 is None:
			while cur_2 is not None:
				cur = cur_2
				cur_2 = cur_2.next
		elif cur_2 is None:
			while cur_1 is not None:
				cur.next = cur_1
				cur_1 = cur_1.next

	def print_l(self):
		temp = self.head
		while temp is not None:
			print temp.data,
			temp = temp.next


def merge_linked_list_recursive(head1, head2):
	head = None
	if head1 is None:
		return head2
	if head2 is None:
		return head1
	if head1.data <= head2.data:
		head = head1
		head.next = merge_linked_list_recursive(head1.next, head2)
	else:
		head = head2
		head.next = merge_linked_list_recursive(head1, head2.next)
	return head


def merge_linked_list_iterative(head1, head2):
	dummy = Node(0)
	tail = dummy
	while True:
		if head1 is None:
			tail.next = head2
			break
		if head2 is None:
			tail.next = head1
			break
		if head1.data <= head2.data:
			tail.next = head1
			head1 = head1.next
		else:
			tail.next = head2
			head2 = head2.next
		tail = tail.next
	return dummy.next


if __name__ == "__main__":
	l1 = LinkedList()
	l1.head = Node(3)
	l1.head.next = Node(5)
	l1.head.next.next = Node(7)
	l1.head.next.next.next = Node(8)
	l1.print_l()

	l2 = LinkedList()
	l2.head = Node(1)
	l2.head.next = Node(4)
	l2.head.next.next = Node(6)
	l2.head.next.next.next = Node(9)
	print
	l2.print_l()

	l3 = LinkedList()
	l3.head = merge_linked_list_recursive(l1.head, l2.head)
	print
	l3.print_l()

	l1 = LinkedList()
	l1.head = Node(3)
	l1.head.next = Node(5)
	l1.head.next.next = Node(7)
	l1.head.next.next.next = Node(8)
	print
	l1.print_l()

	l2 = LinkedList()
	l2.head = Node(1)
	l2.head.next = Node(4)
	l2.head.next.next = Node(6)
	l2.head.next.next.next = Node(9)
	print
	l2.print_l()

	l4 = LinkedList()
	l4.head = merge_linked_list_recursive(l1.head, l2.head)
	print
	l4.print_l()


