#Assuming no repitations
def find_rotation(a):
	n = len(a)
	low =0
	high = n - 1
	while low <= high:
		if a[low] <= a[high]: #case 1
			return low
		mid = (low+high)/2
		next = (mid+1)%n
		prev = (mid+n-1)%n
		if a[mid] <= a[next] and a[mid] <= a[prev]: #case 2
			return mid
		elif a[mid] <= a[high]: #case 3
			high = mid - 1
		elif a[mid] >= a[low]: #case 4
			low = mid + 1
	return -1


if __name__ == "__main__":
	a = [11,12,2,3,4]
	print find_rotation(a)
	a = [11, 12, 13, 14, 2]
	print find_rotation(a)
