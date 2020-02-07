"""
Reference: https://www.geeksforgeeks.org/secretary-problem-optimal-stopping-problem/
"""

# Python3 Program to test 1/e law for
# Secretary Problem
import random
import math

e = 2.71828


# To find closest integer of num.
def roundNo(num):
	if (num < 0):
		return (num - 0.5)
	else:
		return (num + 0.5)

	# Finds best candidate using n/e rule.


# candidate[] represents talents of n candidates.
def printBestCandidate(candidate, n):
	# Calculating sample size for benchmarking.
	sample_size = roundNo(n / e)
	print("\n\nSample size is",
				math.floor(sample_size))

	# Finding best candidate in sample size
	best = 0;
	for i in range(1, int(sample_size)):
		if (candidate[i] > candidate[best]):
			best = i

		# Finding the first best candidate that
	# is better than benchmark set.
	for i in range(int(sample_size), n):
		if (candidate[i] >= candidate[best]):
			best = i
			break

	if (best >= int(sample_size)):
		print("\nBest candidate found is",
					math.floor(best + 1),
					"with talent", math.floor(candidate[best]))
	else:
		print("Couldn't find a best candidate")



if __name__ == "__main__":
	n = 8

	# n = 8 candidates and candidate
	# array contains talents of n
	# candidate where the largest
	# number means highest talented
	# candidate.
	candidate = [0] * (n)

	# generating random numbers between 1 to 8
	# for talent of candidate
	for i in range(n):
		candidate[i] = 1 + random.randint(1, 8)
	print "Candidate : ",

	for i in range(n):
		print (i + 1),
	print "\nTalents : ",

	for i in range(n):
		print candidate[i],

	printBestCandidate(candidate, n)