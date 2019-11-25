def binary_search(a, x):
	low = 0
	high = len(a) - 1
	while low <= high:
		mid = (low + high)/2
		if x == a[mid]:
			return mid
		elif x < a[mid]:
			high = mid - 1
		elif x > a[mid]:
			low = mid + 1
	return -1


def binary_search_first_last_occurence(a, x, occurence="first"):
	low = 0
	high = len(a) - 1
	result_index = -1
	while low <= high:
		mid = (low + high)/2
		if x == a[mid]:
			result_index = mid
			if occurence == "first":
				high = mid -1
			elif occurence == "last":
				low = mid + 1
		elif x < a[mid]:
			high = mid - 1
		elif x > a[mid]:
			low = mid + 1
	return result_index


def binary_search_recursive(a, low, high, x):
	if low <= high:
		mid = (low + high) / 2
		if x == a[mid]:
			return mid
		elif x < a[mid]:
			return binary_search_recursive(a, low, mid - 1, x)
		elif x > a[mid]:
			return binary_search_recursive(a, mid + 1, high, x)
	else:
		return -1


def binary_recursive_first_last_occ(a, low, high, x, ri=-1, occurence="first"):
	#global result_index
	if low <= high:
		mid = (low + high) / 2
		if x == a[mid]:
			#return mid
			if occurence == "first":
				return binary_recursive_first_last_occ(a, low, mid - 1, x, ri=mid, occurence=occurence)
			elif occurence == "last":
				return binary_recursive_first_last_occ(a, mid + 1, high, x, ri=mid, occurence=occurence)
		elif x < a[mid]:
			return binary_recursive_first_last_occ(a, low, mid - 1, x, ri, occurence)
		elif x > a[mid]:
			return binary_recursive_first_last_occ(a, mid + 1, high, x, ri, occurence)
	else:
		return ri


if __name__ == "__main__":
	a = [1,2,3,4,5,6]
	print binary_search(a,4)
	print binary_search_first_last_occurence(a, 4, occurence="first")
	print binary_search_first_last_occurence(a, 4, occurence="last")
	a = [1,2,3,4,4,4,4,5,6]
	print binary_search_first_last_occurence(a, 4, occurence="first")
	print binary_search_first_last_occurence(a, 4, occurence="last")
	#a = [1, 2, 3, 4, 5, 6]
	print binary_recursive_first_last_occ(a, 0, len(a) - 1, 4, ri=-1, occurence="first")
	print binary_recursive_first_last_occ(a, 0, len(a) - 1, 4, ri=-1, occurence="last")
