'''
Find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.

Ex: [-2, -3, 4, -1, -2, 1, 5, -3]

max sum contiguos subarray is 7 [4,-1,-2,1,5]
'''
def max_sum_subarray_n3(a):
	len_a = len(a)
	max_sum = -float('inf')
	for sub_array_size in range(1, len_a + 1):
		for start_index in range(0, len_a):
			if start_index + sub_array_size > len_a:
				break
			sum = 0
			for i in range(start_index, start_index + sub_array_size):
				sum += a[i]
				#print a[i],
			#print
			max_sum = max(max_sum, sum)
	return max_sum


def max_sum_subarray_n2(a):
	len_a = len(a)
	max_sum = -float('inf')
	for start_index in range(0, len_a):
		sum = 0
		for sub_array_size in range(1, len_a + 1):
			if start_index + sub_array_size > len_a:
				break
			sum += a[start_index + sub_array_size - 1]
			#print sum
			max_sum = max(max_sum, sum)
	return max_sum


def max_sum_subarray_nlogn(a,len_a):
	if len_a == 1:
		return a[0]
	m = len_a/2
	left_mss = max_sum_subarray_nlogn(a, m)
	right_mss = max_sum_subarray_nlogn(a, len_a-m)
	left_sum = -float('inf')
	right_sum = -float('inf')
	sum = 0
	for i in range(m, len_a):  # m->n
		sum += a[i]
		right_sum = max(right_sum, sum)
	sum = 0
	for i in range(m-1, -1, -1): # m-1 -> 0
		sum += a[i]
		left_sum = max(left_sum, sum)
	return max(left_mss, right_mss, left_sum+right_sum)


def max_sum_subarray_kadane_n(a):
	max_so_far = -float('inf')
	max_here = 0
	start, end, s = 0,0,0
	for i in range(0, len(a)):
		max_here += a[i]
		if max_so_far < max_here:
			max_so_far = max_here
			start = s
			end = i
		if max_here < 0:
			max_here = 0
			s = i + 1
	print start, end
	return max_so_far


if __name__ == "__main__":
	a = [3,-2,5,1]
	print "Max sum of sub array is with O(n3)", max_sum_subarray_n3(a)
	print "Max sum of sub array is with O(n2)", max_sum_subarray_n2(a)
	print "Max sum of sub array is with O(nlogn)", max_sum_subarray_nlogn(a, len(a))
	print "Max sum of sub array is with O(n)", max_sum_subarray_kadane_n(a)
	print max_sum_subarray_kadane_n([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] )