str = raw_input("enetr the string")
rem = raw_input("enetr the string to remove")
output = list()
ls = list(str)
lr = list(rem)

#print rem.index('x')

for i in ls :
    try:
        if lr.index(i) > 0:
            pass
    except:
        output.append(i)    
        
print "".join(output)
        
        