num = raw_input()
numbers = tuple(map(int,raw_input().split()))
dup = set(numbers)
dup_rem_l = list(dup)


dup_rem_l.sort()
dup_rem_l.reverse()

print dup_rem_l[1]
