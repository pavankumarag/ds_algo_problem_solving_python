
'''Problem : Write an efficient function to find the first nonrepeated character in a string. 
For instance, the first nonrepeated character in “total” is 'o' 
and the first nonrepeated character in "teeter" is 'r'. 
'''
str = raw_input("Enter the string")
rep = {}  # or can be declared as dict()

for ch in str :
    if ch in rep.keys():
        rep[ch] =+ 1
    else:
        rep[ch] = 0

for ch in str:
    if rep[ch] == 0:
        print "The first non repeated character in the given string %s is %r" %(str,ch)
        break
    

    