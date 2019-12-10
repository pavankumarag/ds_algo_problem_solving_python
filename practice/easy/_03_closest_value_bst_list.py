def closest_value_in_list_logn_my_try(a, k):
	# assuming a is sorted
	if len(a) == 0:
		return None
	elif len(a) == 1:
		return a[0]
	else:
		closest_val = dict()
		min_diff = float('inf')
		left_mid_diff = None
		right_mid_diff = None
		low = 0
		high = len(a) - 1
		while low < high:
			mid = (low + high)/2
			mid_diff = abs(k - a[mid])
			if mid + 1 <= high: # checking we are not crossing array bounds
				right_mid_diff = abs(k - a[mid + 1])
			if mid - 1 >= low: # checking we are not crossing array bounds
				left_mid_diff = abs(k - a[mid - 1])
			# if a[mid] is closest so as to avoid going further
			if a[mid] == k or (mid_diff < right_mid_diff and mid_diff < left_mid_diff):
				closest_val.clear()
				closest_val.setdefault(a[mid])
				break
			elif mid_diff == right_mid_diff: # if there are two closest for k
				closest_val.clear()
				closest_val.setdefault(a[mid])
				closest_val.setdefault(a[mid+1])
				break
			elif mid_diff == left_mid_diff: # if there are two closest for k
				closest_val.clear()
				closest_val.setdefault(a[mid])
				closest_val.setdefault(a[mid-1])
				break
			elif right_mid_diff < left_mid_diff: # decide which half of array to discard
				if right_mid_diff < min_diff:
					min_diff = right_mid_diff
					closest_val.clear()
					closest_val.setdefault(a[mid+1])
				low = mid + 1
			elif left_mid_diff < right_mid_diff:
				if left_mid_diff < min_diff:
					min_diff = left_mid_diff
					closest_val.clear()
					closest_val.setdefault(a[mid-1])
				high = mid - 1
			elif right_mid_diff == left_mid_diff: # check if two closest match
				closest_val.clear()
				closest_val.setdefault(a[mid+1])
				closest_val.setdefault(a[mid-1])
				break
		return closest_val.keys()


def closest_val_in_lst_logn(a, k):
	if len(a) == 0:
		return None
	if len(a) == 1:
		return a[1]
	low = 0
	high = len(a) - 1
	min_diff = float("inf")
	right_mid_diff = None
	left_mid_diff = None
	closest_val = None
	mid_diff = None
	while low <= high:
		# calculate mid_diff, right_mid_diff, left_mid_diff to check the closest match
		mid = (low + high) / 2
		if mid+1 < len(a):
			right_mid_diff = abs(k - a[mid+1])
		if mid > 0:
			left_mid_diff = abs(k - a[mid-1])
		mid_diff = abs(k - a[mid])
		if mid_diff == right_mid_diff and mid+1 < len(a): # check two closest for k
				return [a[mid], a[mid+1]]
		elif mid_diff == left_mid_diff and mid < 0: # check two closest for k
			return [a[mid-1], a[mid]]
		if right_mid_diff < min_diff: # min_diff = lowest(min_diff, right_mid_diff, left_mid_diff)
			min_diff = right_mid_diff
			closest_val = a[mid + 1]   # and update closest respectively
		if left_mid_diff < min_diff:
			min_diff = left_mid_diff
			closest_val = a[mid - 1]
		# Binarty search decisions
		if k > a[mid]:
			low = mid + 1
		elif k < a [mid]:
			high = mid - 1
		elif k == a[mid]:
			return a[mid]
		print
	return closest_val


class BSTNode:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None


class Solutions:
	def recursive_closest_val(self, root, val):
		# start with closest = root.data, last argument
		return self.binary_search(root, val, root.data)

	@staticmethod
	def closest_val(root, val):
		closest = root.data
		while root:
			if abs(root.data - val) < abs(val - closest): # check on root.data is closest
				closest = root.data
			if val < root.data : root = root.left
			else: root = root.right
		return closest

	def binary_search(self, root, val, closest):
		if not root:
			return closest
		if abs(root.data - val) < abs(val - closest): # check on root.data is closest
			closest = root.data
		if val < root.data: return self.binary_search(root.left, val, closest)
		elif val > root.data: return self.binary_search(root.right, val, closest)
		return closest

	def find_closest_val(self, root, k):
		min_diff = float('inf') # same as we did for list
		min_diff_key = [-1]
		self.find_closest_helper(root, k, min_diff, min_diff_key)
		return min_diff_key[0]

	def find_closest_helper(self, root, k, min_diff, min_diff_key):
		if root is None: return
		if root.data == k:
			min_diff_key[0] = root.data
			return
		if min_diff > (root.data - k): # check if root has closest element
			min_diff = root.data - k
			min_diff_key[0] = root.data
		if k < root.data:
			self.find_closest_helper(root.left, k, min_diff, min_diff_key)
		else:
			self.find_closest_helper(root.right, k, min_diff, min_diff_key)


if __name__ == "__main__":
	a = [2,4,7,11,17,19,23,30]
	k = 19
	# print closest_value_in_list_logn_my_try(a, k)
	import timeit
	print timeit.timeit("closest_value_in_list_logn_my_try([2,4,5,11,17,19,23,30],12)",
								setup="from __main__ import closest_value_in_list_logn_my_try",
								number=1)
	print timeit.timeit("closest_val_in_lst_logn([2,4,5,11,17,19,23,30],12)",
								setup="from __main__ import closest_val_in_lst_logn",
								number=1)
	print closest_val_in_lst_logn(a, k)
	root = BSTNode(9)
	root.left = BSTNode(4)
	root.left.left = BSTNode(3)
	root.right = BSTNode(17)
	root.right.right = BSTNode(22)
	root.right.right.left = BSTNode(20)
	root.left.right = BSTNode(6)
	root.left.right.left = BSTNode(5)
	root.left.right.right = BSTNode(7)
	s = Solutions()
	print s.recursive_closest_val(root, 6)
	print Solutions.closest_val(root, 6)
	print s.find_closest_val(root, 6)




