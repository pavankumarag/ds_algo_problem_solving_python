'''
Method 1 -> linear search of ele and count until you reach ele greater than ele: Takes O(n) in worst case
Method 2 -> Binary search and search left until an ele less is found and search right until ele greater is found
this takes O(logn) + O(n) in worst case if all array elements are ele. so O(n) as O(logn) is negligible for larger
value of n
Method 3 -> Using variation of binary search. Find the first occurrence of ele and find the last occurence of ele
and then last - first + 1. This takes O(logn) + O(logn) + 1 = O(logn)
'''
import env
from Binary_search_all_variants import binary_search_first_last_occurence
if __name__ == "__main__":
	a = [1,2,3,3,4,4,4,4,8,9]
	first = binary_search_first_last_occurence(a, 3, occurence="first")
	last = binary_search_first_last_occurence(a, 3, occurence="last")
	print last - first + 1
