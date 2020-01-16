"""
Tower of Honoi
we have three rods and n disks the objective of the puzzle is to move the entire stack to another rod,
obeying the following simple rules:
1) Only one disk can be moved at a time.
2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e.
 a disk can only be moved if it is the uppermost disk on a stack.
3) No disk may be placed on top of a smaller disk.
"""


def tower_of_honoi(n, from_rod, to_rod, aux_rod):
	if n == 1:
		print "Move disk 1 from ", from_rod, "to ", to_rod
		return
	tower_of_honoi(n-1, from_rod, aux_rod, to_rod)
	print "Move disk",n, "from ", from_rod, "to ", to_rod
	tower_of_honoi(n-1, aux_rod, to_rod, from_rod)


if __name__ == "__main__":
	n = 4
	tower_of_honoi(n, 'A', 'C', 'B')