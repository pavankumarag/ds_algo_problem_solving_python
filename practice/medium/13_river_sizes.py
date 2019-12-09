'''
you are given two dimensional array(matrix) of potentially unequal height and width containing only 0s and 1s. Each 0
represent land and each 1 represent part of land. A river consists of any number of 1s that are either horizontally or
vertically adjacent( but not diagonally adjacent). The number of adjacent 1s forming a river determine its sizes.
Write a function that returns an array of the sizes of all the rivers represented in the input matrix. Note that these
sizes do not need to be in any particular order.

Sample input
[
[1,0,0,1,0],
[1,0,1,0,0],
[0,0,1,0,1],
[1,0,1,0,1],
[1,0,1,1,0]
]

output
[1,2,2,2,5]
'''


def river_sizes(matrix):
	sizes = []
	visited = [[False for value in row] for row in matrix]
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if visited[i][j]:
				continue
			traverse_node(i, j, matrix, visited, sizes)
	return sizes


def traverse_node(i, j, matrix, visited, sizes):
	current_river_size = 0
	nodes_to_explore = [[i, j]]
	while len(nodes_to_explore):
		current_node = nodes_to_explore.pop()
		i = current_node[0]
		j = current_node[1]
		if visited[i][j]:
			continue
		visited[i][j] = True
		if matrix[i][j] == 0:
			continue
		current_river_size += 1
		unvisited_neighbours = get_unvisited_neighbours(i, j, matrix, visited)
		for neighbour in unvisited_neighbours:
			nodes_to_explore.append(neighbour)
	if current_river_size > 0:
		sizes.append(current_river_size)


def get_unvisited_neighbours(i, j, matrix, visited):
	unvisited_neighbours = []
	if i > 0 and not visited[i-1][j]:
		unvisited_neighbours.append([i-1, j])
	if i < len(matrix) - 1 and not visited[i+1][j]:
		unvisited_neighbours.append([i+1, j])
	if j > 0 and not visited[i][j-1]:
		unvisited_neighbours.append([i, j-1])
	if j < len(matrix[0]) - 1 and not visited[i][j+1]:
		unvisited_neighbours.append([i, j+1])
	return unvisited_neighbours


if __name__ == "__main__":
	a = [
[1,0,0,1,0],
[1,0,1,0,0],
[0,0,1,0,1],
[1,0,1,0,1],
[1,0,1,1,0]
]
print river_sizes(a)