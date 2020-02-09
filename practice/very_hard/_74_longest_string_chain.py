"""
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it
equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2,
 word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.


Example

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
"""


class Solution:
	def longestStrChain(self, words):

		# need to create a special dictionary to hold the predecessor and the length
		# of the longest word chain ending with that word

		# are the words asorted in words? Assume no -> sort
		words.sort(key=lambda x: len(x))
		# since we are using the values computed beforehand,  this is a dynamic problem
		dp = {word: ('', 1) for word in words}

		for word in words:
			for i in range(len(word)):
				temp = word[:i] + word[i + 1:]
				if temp in dp:
					dp[word] = (temp, max(dp[word][1], dp[temp][1] + 1))
				continue

		# now our dp dictionary containes precomputed word chains for each of the words in the dictionary keys
		# need to return the length of the longes one
		res = [v for v in sorted(dp.values(), key=lambda x: x[1], reverse=True)]
		return res[0][1]


# import queue
class Solution2:  # python 3 solution
	"""
	1.The word-chain has a nice property: each predecessor differing in length by exactly 1 compared to the next word in
	the chain
	2.Predecessors->word is a many-1 relation. To be exact you can insert 26 chars at any position in the predecessor
	to get to a potential successor
	3.Its expensive to link predecessor to successor (esp with 1000 words-> 1000^2 operations). But the other way round
	is very quick.
	4. For each word, remove 1 char from any position to achieve a potential predecessor =>O(N*16) => O(N) operation to
	formulate the adjacency-list for the graph.
	For example, for word "abcd" -> "bcd", "acd", "abc" are the only potential predecessors
	5. Identify all the nodes with 0 incoming edges (largest-size words) and run a simple BFS for each of these
	starting-points and find the one with the largest word-link
	"""

	def longestStrChain(self, words):
		emap = dict()
		dmap = dict()
		wset = set(words)
		for word in words:
			vlist = []
			for i in range(len(word)):
				pred_word = word[:i] + word[i + 1:]
				if pred_word in wset:
					vlist.append(pred_word)
			emap[word] = vlist
			for v in vlist:
				if v not in dmap:
					dmap[v] = 0
				dmap[v] += 1

		start_words = []
		for word in words:
			if word not in dmap or dmap[word] == 0:
				start_words.append(word)

		maxl = 0
		for word in start_words:
			bq = queue.Queue()
			bq.put((word, 1))
			while bq.qsize() > 0:
				pword, depth = bq.get()
				maxl = max(maxl, depth)
				if pword not in emap:
					continue
				for v in emap[pword]:
					bq.put((v, depth + 1))
		return maxl


class Solution3:
	"""
	Initially, each word's longest chain is set to 1. Then, we loop the list of words to find out whether it has a
	predecessor in the list. If there is a predecessor, we know current word's longest chain could be predecessor's
	longest chain plus one.

There are two main points for this solution:

1. Sort the word list words by each length of the word.
As mentioned above, current word's longest chain is formed by predecessor's longest chain plus one.
Therefore, we must calculate the predecessor's longest chain first, otherwise the answer would be incorrect.

2.Comparing the current word's chain with all its predecessor's longest chain plus one to find out the current word's
longest chain.This is because the current word's chain could possibly be formed in many different ways, so we need to
compare them to find out the longest one.
	"""
	def longestStrChain(self, words):
		d = dict()
		for word in words:
			d[word] = 1
		longest = 1
		for word in sorted(words, key=len):
			for i in range(len(word)):
				prev = word[:i] + word[i + 1:]
				if prev in d:
					d[word] = max(d[word], d[prev] + 1)
			longest = max(longest, d[word])
		return longest


if __name__ == "__main__":
	words = ["a", "b", "ba", "bca", "bda", "bdca"]
	s = Solution()
	print s.longestStrChain(words)
	# s1 = Solution2()
	# print s1.longestStrChain(words)
	s2 = Solution3()
	print s2.longestStrChain(words)
