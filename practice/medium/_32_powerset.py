"""
Power set P(S) of a set S is the set of all subsets of S. For example S = {a, b, c} then
P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.

If S has n elements in it then P(s) will have 2^n elements

https://rosettacode.org/wiki/Power_set#Python
https://www.geeksforgeeks.org/power-set/
"""
import math

class Solutions:
	def __init__(self, inp_str):
		self.inp_str = inp_str
		self.out = ""
		self.res = set()

	def powerset(self, start):
		'''
		This is also combinationsOfString
		:param start:
		:return:
		'''
		for i in range(start, len(self.inp_str)):
			self.out = self.out + self.inp_str[i]
			self.res.add(self.out)
			if i < len(self.inp_str):
				self.powerset(i+1)
			self.out = self.out[0:len(self.out)-1]
		self.res.add('')
		return self.res

	def powerset_binary(self, set_size):
		"""
		Set  = [a,b,c]
		power_set_size = pow(2, 3) = 8
		Run for binary counter = 000 to 111

		Value of Counter            Subset
    	000                    -> Empty set
    	001                    -> a
    	010                    -> b
    	011                    -> ab
    	100                    -> c
    	101                    -> ac
    	110                    -> bc
    	111                    -> abc
		:param set_size:
		:return:
		"""
		pw_set_size = int(math.pow(2, set_size))
		for counter in range(0, pw_set_size):
			for j in range(0,set_size):
				if counter & (1 << j) > 0: # Check if jth bit in the counter is set If set then print jth element from set
					print self.inp_str[j],
			print

	def list_powerset(self, lst):
		# the power set of the empty set has one element, the empty set
		result = [[]]
		for x in lst:
			# for every additional element in our set
			# the power set consists of the subsets that don't
			# contain this element (just take the previous power set)
			# plus the subsets that do contain the element (use list
			# comprehension to add [x] onto everything in the
			# previous power set)
			result.extend([subset + [x] for subset in result])
		return result

	# the above function in one statement
	def list_powerset2(self, lst):
		return reduce(lambda result, x: result + [subset + [x] for subset in result],
									lst, [[]])

	def powerset_frozenset(self, s):
		return frozenset(map(frozenset, self.list_powerset(list(s))))

	def powerset_recursive(self, l):
		if not l: return [[]]
		return self.powerset_recursive(l[1:]) + [[l[0]] + x for x in self.powerset_recursive(l[1:])]


if __name__ == "__main__":
	s = Solutions("abc")
	print s.powerset(0)
	s.powerset_binary(len(s.inp_str))
	print s.list_powerset([1,2,3])
	print s.list_powerset2([1,2,3])
	print s.powerset_frozenset(frozenset([1,2,3]))
	print s.powerset_recursive([1,2,3])