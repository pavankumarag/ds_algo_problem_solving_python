a = [1,2,3,4,1,2,3,4,5]

element = 0

for i in range(len(a)):
    element = element ^ a[i]
    
print element