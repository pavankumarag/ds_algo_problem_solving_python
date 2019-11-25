import sys
from collections import defaultdict

val = raw_input('ENter the num of students')
var = defaultdict(list)
num = int(val)
print num
'''
while isinstance(val,int) != True :
    try :
        num = int(val)
    except :
        print "Please enter integer value"
        val = raw_input('ENter the num of students > ')
'''

for i in range(0,num):
    name = raw_input('Enter the student name >')
    var[name].append(int(raw_input('Enter the math marks >')))
    var[name].append(int(raw_input('Enter the phy marks >')))
    var[name].append(int(raw_input('Enter the che marks >')))

print var.items()
print var.keys()
print var.values()

input_v = raw_input("ENter the student name to see his details")

if input_v in var.keys():
    summ = 0
    for i in var[input_v]:
        summ += i
    Avg = summ / len(var[input_v])
    print "Average of student %r is %r" %(input_v,Avg)
else:
    print "The requested student details doesnt exists"
    
'''        
for k in var :
    print var[k]
    summ = 0
    for i in v:
        summ += i
    print  "  is ",summ
    '''
    
'''
hackerrank expectation

n=int(raw_input())

dic={}

for i in range(n):
    line=raw_input().split()
    dic[line[0]]=sum(map(float,line[1:]))/3.0

print '%.2f' % dic[raw_input()]

'''



