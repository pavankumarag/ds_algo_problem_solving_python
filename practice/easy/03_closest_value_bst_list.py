def closest_value_in_list(a, k):
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
			if mid + 1 <= high:
				right_mid_diff = abs(k - a[mid + 1])
			if mid - 1 >= low:
				left_mid_diff = abs(k - a[mid - 1])
			if a[mid] == k or (mid_diff < right_mid_diff and mid_diff < left_mid_diff):
				closest_val.clear()
				closest_val.setdefault(a[mid])
				break
			elif mid_diff == right_mid_diff:
				closest_val.clear()
				closest_val.setdefault(a[mid])
				closest_val.setdefault(a[mid+1])
				break
			elif mid_diff == left_mid_diff:
				closest_val.clear()
				closest_val.setdefault(a[mid])
				closest_val.setdefault(a[mid-1])
				break
			elif right_mid_diff < left_mid_diff:
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
			elif right_mid_diff == left_mid_diff:
				closest_val.clear()
				closest_val.setdefault(a[mid+1])
				closest_val.setdefault(a[mid-1])
				break
		return closest_val.keys()


if __name__ == "__main__":
	a = [2,4,9,11,12,19,23,30]
	k = -1
	print closest_value_in_list(a, k)


