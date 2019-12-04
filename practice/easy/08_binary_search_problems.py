
def binary_search(a, ele, occurence="default"):
	low = 0
	high = len(a) - 1
	index = -1
	while low <= high:
		mid = (low + high) / 2
		if a[mid] == ele:
			index = mid
			if occurence == "default":
				return index
			elif occurence == "first":
				high = mid -1
			elif occurence == "last":
				low = mid + 1
		elif ele > a[mid]:
			low = mid + 1
		else:
			high = mid - 1
	return index


def binary_search_rec(a, low, high, ele, ri=-1, occurence="default"):
	if low <= high:
		mid = (low + high)/2
		if a[mid] == ele:
			if occurence == "default":
				return mid
			elif occurence == "first":
				return binary_search_rec(a, low, mid-1, ele, ri=mid, occurence=occurence)
			elif occurence == "last":
				return binary_search_rec(a, mid+1, high, ele, ri=mid, occurence=occurence)
		elif ele > a[mid]:
			return binary_search_rec(a, mid+1, high, ele, ri, occurence)
		else:
			return binary_search_rec(a, low, mid-1, ele, ri, occurence)
	else:
		return ri


def count_of_ele_in_sorted_list(a, ele):
	first = binary_search(a, ele, occurence="first")
	last = binary_search(a, ele, occurence="last")
	return (last - first + 1)


def find_num_of_rotation(a):
	low = 0
	n = len(a)
	high = n - 1
	while low <= high:
		if a[low] < a[high]:  # case 1: not rotated at all
			return low
		mid = (low + high) / 2
		next = (mid + 1) % n
		prev = (mid + n - 1) % n
		if a[mid] <= a[next] and a[mid] <= a[prev]:  # case 2: find that mergning point in rotated array
			return mid
		elif a[mid] >= a[low]: # case3: one part of the array is sorted but pivot lies in non-sorted part
			low = mid + 1
		elif a[mid] <= a[high]: # case4: one part of the array is sorted but pivot lies in non-sorted part
			high = mid - 1
	return -1


def find_in_sorted_array(a, ele):
	low = 0
	high = len(a) - 1
	while low <= high:
		mid = (low + high)/2
		if a[mid] == ele: # case 1 found x at mid position
			return mid
		if a[mid] <= a[high]: # case 2 right half is sorted
			if ele <= a[high] and ele > a[mid]:
				low = mid + 1 # go search in right sorted half
			else:
				high = mid - 1
		elif a[low] <= a[mid]: # case 3 left half is sorted
			if ele < a[mid] and ele >= a[low]:
				high = mid - 1  # go search in left sorted half
			else:
				low = mid + 1
	return -1


if __name__ == "__main__":
	a = [3,8,12,12,12,12,14,14,16]
	ele = 14
	print binary_search(a, ele, occurence="last")
	print binary_search_rec(a, 0, len(a)-1, ele, ri=-1, occurence="first")
	first = binary_search(a, ele, occurence="first")
	last = binary_search(a, ele, occurence="last")
	print "Number of occurence of %d is %d" %(ele, (last - first + 1))
	print "Number of occurence of %d is %d" %(ele, count_of_ele_in_sorted_list(a, ele))
	a = [11, 12, 2, 3, 4]
	print find_num_of_rotation(a)
	a = [11, 12, 13, 14, 2]
	print find_num_of_rotation(a)
	a = [12, 13, 14, 2, 3, 4]  # no duplicates, if duplicates then needs linear search
	print find_in_sorted_array(a, 13)
	print find_in_sorted_array(a, 3)
