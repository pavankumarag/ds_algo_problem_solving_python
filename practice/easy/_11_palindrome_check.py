def palindrome_check_str(strr):
	lenn = len(strr)
	start = 0
	end = lenn - 1
	while start < lenn and end >= 0:
		if strr[start] != strr[end]:
			return False
		if lenn %2 != 0 and start == end:
			# Avoid traversing whole length as we hit the half value mark for odd length string"
			return True
		elif lenn %2 == 0 and start+1 == end and strr[start+1] == strr[end]:
			# Avoid traversing whole length as we hit the half value mark for even length string"
			return True
		start += 1
		end -= 1
	return True


def palindrome_check_num(num):
	numm = num
	rev = 0
	poww = 0
	while num > 0:
		rem = num % 10
		num = num / 10
		rev = rev * 10 + rem
		poww += 1
	if numm == rev:
		return True
	else:
		return False


def palindrome_check_gen(_input):
	if type(_input) is int:
		_input = str(_input)


if __name__ == "__main__":
	print palindrome_check_str("nayan")
	print palindrome_check_str("pavan")
	print palindrome_check_str("pavannavap")
	print palindrome_check_str("pavabnavap")
	print palindrome_check_num(141)
	print palindrome_check_num(123321)
	print palindrome_check_num(123)


