
#interchange the case
input_string = raw_input()
str_list = list(input_string)


'''
for ch in str_list:
    if ch.isupper():
         ch = ch.lower()
    elif ch.isupper():
        ch = ch.upper()
    else:
        pass
'''

for i in range(len(str_list)):
    if str_list[i].isalpha():
        if str_list[i].isupper():
            str_list[i] = str_list[i].lower()
        elif str_list[i].islower():
            str_list[i] = str_list[i].upper()
        else:
            pass

#print str_list
    
print "".join(str_list)

'''
Other solution

print raw_input().swapcase()
'''