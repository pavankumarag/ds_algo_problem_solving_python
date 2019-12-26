class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


def insert_at_beginning(head, val):
	if head is None:
		head = Node(val)
		return head
	new_node = Node(val)
	new_node.next = head
	head = new_node
	return head


def print_list(head):
	curr = head
	while curr is not None:
		print curr.data,
		curr = curr.next


def delete_nth_at_end(head, n):
	'''
	Brute force method, where count the number of node and delete from the delete from the beginning
	:param head:
	:param n:
	:return:
	'''
	count = 1
	curr = head
	while curr.next is not None:
		count += 1
		curr = curr.next
	k = count - n + 1
	if k > 1:
		temp = head
		count = 1
		while count < k - 1:
			temp = temp.next
			count += 1
		print "Node deleted is ", temp.next.data
		temp.next = temp.next.next
	elif k == 1:
		print "Node deleted is ", head.data
		head = head.next
	else:
		print "Please enter valid position"
		return -1
	return head


def delete_nth_at_end_optimised(head, n):
	first = second = head
	for i in range(n):
		if second.next is None:
			# If count of nodes in the given list is less than 'n'
			if i == n-1: # If index = n then delete the head node
				head = head.next
			return head
		second = second.next
	while second.next is not None:
		second = second.next
		first = first.next
	print "\nNode deleted is", first.next.data
	first.next = first.next.next
	return head


if __name__ == "__main__":
	head = insert_at_beginning(None, 2)
	head = insert_at_beginning(head, 3)
	head = insert_at_beginning(head, 4)
	head = insert_at_beginning(head, 5)
	head = insert_at_beginning(head, 6)
	head = insert_at_beginning(head, 7)
	print_list(head)
	print
	head = delete_nth_at_end(head, 3)
	print
	print_list(head)
	head = insert_at_beginning(head, 8)
	print
	print_list(head)
	head = delete_nth_at_end_optimised(head, 3)
	print
	print_list(head)


