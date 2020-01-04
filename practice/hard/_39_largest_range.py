"""
Largest Range

Given an array of integers return an array of length 2 representing the largest range of numbers contained
in the array. For instance array result [2,6] represents the range [2,3,4,5,6]  of length 5.

Note that numbers need not to be adjacent in ordered to be part of the range.

Example:
input : [1,11,3,0,15,5,2,4,10,7,12,6]
output: [0,7]
"""


def largest_range(a): # Takes nlogn + n = nlogn
	a.sort()
	di = dict()
	for i in range(0,len(a)):
		if i == 0:
			first = a[i]
		if i+1 < len(a) and a[i] + 1 == a[i+1]:
			continue
		else:
			last = a[i]
			di[last - first + 1] = [first, last]
			if i+1 < len(a):
				first = a[i+1]
	return di[max(di.keys())]


def largest_range_n(a): # Takes O(n) time and O(n) space
	longest_length  = 0
	best_range = []
	nums = dict()
	for num in a:
		nums[num] = True
	for num in a:
		if not nums[num]:
			continue
		nums[num] = False
		current_length = 1
		left = num - 1
		right = num + 1
		while left in nums:
			nums[left] = False
			left -= 1
			current_length += 1
		while right in nums:
			nums[right] = False
			right += 1
			current_length += 1
		if current_length > longest_length:
			longest_length = current_length
			best_range = [left+1, right-1]
	return best_range


if __name__ == "__main__":
	print largest_range([1,11,3,0,15,5,2,4,10,7,12,6])
	print largest_range([3,5,9,8,6,4,10,1,7])
	print largest_range_n([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6])
	print largest_range_n([3, 5, 9, 8, 6, 4, 10, 1, 7])

