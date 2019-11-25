# Enter your code here. Read input from STDIN. Print output to STDOUT
a= set()
b= set()
for i in range(2):
    line = raw_input()
    lis = line.split()
    #print lis
    new_lis = list(map(int,lis))
    #print new_lis
    for i in new_lis:
        a.add(i)
    
print a
for i in range(2):
    line = raw_input()
    lis = line.split()
    new_lis = list(map(int,lis))
    for i in new_lis:
        b.add(i)
   
#print a,b

print a.difference(b)
print b.difference(a)

final = list(a.difference(b))

for i in sorted(final):
    print i
    
for i in sorted(list(b.difference(a))):
    print i



'''input


4
2 4 5 9
4
2 4 11 12



output

5
9
11
12

'''