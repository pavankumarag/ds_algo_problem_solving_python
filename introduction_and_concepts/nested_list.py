from operator import itemgetter
num = int(raw_input())
students = list()

for i in range(num):
   temp = [ raw_input(),float(raw_input())]
   students.append(temp)

newlist = sorted(students,key=itemgetter(1))

lowest = newlist[0][1]

for i in newlist:
    if i[1] == lowest:
        newlist.remove(i)

sec_low = newlist[0][1]
sec_low_names = list()
for i in newlist:
    if i[1] == sec_low :
        sec_low_names.append(i[0])

for i in sorted(sec_low_names):
    print str(i)
    
    
'''
   Input 
   5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39


OUTPUT
Berry
Harry

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

 
'''