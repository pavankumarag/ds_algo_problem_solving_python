# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(raw_input())
L = []
for i in range(num):
    line = raw_input().split()
    #print line
    if line[0] == "insert":
        a = int(line[1])
        b = int(line[2])
        L.insert(a,b)
    elif line[0] == "print":
        print L
    elif line[0] == "append":
        L.append(int(line[1]))
    elif line[0] == "remove":
        L.remove(int(line[1]))
    elif line[0] == "pop":
        L.pop()
    elif line[0] == "reverse":
        L.reverse()
    elif line[0] == "sort":
        L.sort()
    else :
        pass
    
''' input
12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print
'''