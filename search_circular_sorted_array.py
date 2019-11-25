def circular_search(a, x):
	low = 0
	high = len(a) - 1
	while low <= high:
		mid = (low+high)/2
		if x == a[mid]:  #case 1 found x at mid position
			return mid
		if a[mid] <= a[high]: # case 2 right half is sorted
			if x > a[mid] and x <= a[high]:
				low = mid + 1	 # go search in right sorted half
			else:
				high = mid - 1
		elif a[mid] >= a[low]: # case 3 left half is sorted
			if x >= a[low] and x < a[mid]:
				high = mid - 1 # go search in left sorted half
			else:
				low = mid + 1

if __name__ == "__main__":
	a = [12,13,14,2,3,4]  # no duplicates, if duplicates then needs linear search
	print circular_search(a, 13)
	print circular_search(a, 3)

