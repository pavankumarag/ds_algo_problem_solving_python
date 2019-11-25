# from graph import Graph
from ADT.graphs_ADT.graph import Graph


def buildGraph(wordFile):
	d = {}
	g = Graph()
	wfile = open(wordFile, 'r')
	# create buckets of words that differ by one letter
	for line in wfile:
		word = line[:-1]
		for i in range(len(word)):
			bucket = word[:i] + '_' + word[i + 1:]
			if bucket in d:
				d[bucket].append(word)
			else:
				d[bucket] = [word]
	# add vertices and edges for words in the same bucket
	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1 != word2:
					g.addEdge(word1, word2)
	return g
