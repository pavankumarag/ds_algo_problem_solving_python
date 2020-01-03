"""
A suffix tree is a data structure commonly used in string algorithms.

Given a string S of length n, its suffix tree is a tree T such that:

T has exactly n leaves numbered from 1 to n.
Except for the root, every internal node has at least two children.
Each edge of T is labelled with a non-empty substring of S.
No two edges starting out of a node can have string labels beginning with the same character.
The string obtained by concatenating all the string labels found on the path from the root to leaf i
spells out suffix S[i..n], for i from 1 to n.

Such a tree does not exist for all strings. To ensure existence, a character that is not found in
S must be appended at its end. The character '$' is traditionally used for this purpose.

https://rosettacode.org/wiki/Suffix_tree#Python
https://www.geeksforgeeks.org/ukkonens-suffix-tree-construction-part-1/
"""


class Node:
	def __init__(self, sub="", children=[]):
		self.sub = sub
		self.ch = children


class Suffix_tree:
	def __init__(self, str):
		self.nodes = [Node()]
		for i in range(len(str)):
			self.add_suffix(str[i:])

	def add_suffix(self, suf):
		n = 0
		i = 0
		while i < len(suf):
			b = suf[i]
			x2 = 0
			while True:
				children = self.nodes[n].ch
				if x2 == len(children):
					# no matching child, remainder of suf becomes new node
					n2 = len(self.nodes)
					self.nodes.append(Node(suf[i:], []))
					self.nodes[n].ch.append(n2)
					return
				n2 = children[x2]
				if self.nodes[n2].sub[0] == b:
					break
				x2 = x2 + 1

			# find prefix of remaining suffix in common with child
			sub2 = self.nodes[n2].sub
			j = 0
			while j < len(sub2):
				if suf[i+j] != sub2[j]:
					# split n2
					n3 = n2
					# new node for the part in common
					n2 = len(self.nodes)
					self.nodes.append(Node(sub2[:j], [n3]))
					self.nodes[n3].sub = sub2[j:]  # old node loses the part in common
					self.nodes[n].ch[x2] = n2
					break  # continue down the tree
				j = j + 1
			i = i + j # advance past part in common
			n = n2  # continue down the tree

	def visualize(self):
		if len(self.nodes) == 0:
			print "<empty>"
			return

		def f(n, pre):
			children = self.nodes[n].ch
			if len(children) == 0:
				print "--", self.nodes[n].sub
				return
			print "+-", self.nodes[n].sub
			for c in children[:-1]:
				print pre, "+-",
				f(c, pre + " | ")
			print pre, "+-",
			f(children[-1], pre + "  ")

		f(0, "")


if __name__ == "__main__":
	Suffix_tree("banana$").visualize()