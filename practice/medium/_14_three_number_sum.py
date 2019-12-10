'''
Given an array of distinct elements. The task is to find triplets in array whose sum is zero.
'''
import env
from practice.easy._02_two_sum import two_sum_n


def three_num_sum_n3(a):
	for i in range(len(a)-2):
		for j in range(i+1, len(a)-1):
			for k in range(j+1, len(a)):
				if a[i] + a[j] + a[k] == 0:
					print a[i], a[j], a[k]
					return True
	return False


def three_num_sum_n2(a):
	# deducing to two_sum problem
	for i in range(len(a)-2):
		ret = two_sum_n(a[i+1:], -a[i])
		if len(ret):
			print a[i], ret
			return True
	return False


def three_num_sum_n2_method2(a):
	# using quick sort logic
	a.sort()
	n = len(a)
	found = False
	for i in range(n-1):
		k = a[i]
		l = i+1
		r = n-1
		if k + a[l] + a[r] == 0:
			found = True
			print k, a[l], a[r]
			l += 1
			r -= 1
		elif k + a[l] + a[r] < 0:
			l += 1
		else:
			r -= 1
	return found


if __name__ == "__main__":
	a = [-4,2,1,6,5,7]
	print three_num_sum_n3(a)
	print three_num_sum_n2(a)
	print three_num_sum_n2_method2(a)
	a = [4,2,2,6,-5,-1]
	print three_num_sum_n3(a)
	print three_num_sum_n2(a)
	print three_num_sum_n2_method2(a)
