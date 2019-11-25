s = raw_input("Enter the space delimited sentence\n")

ls = s.split(" ")
ls.reverse()
res = str()
start = 0
for ele in ls:
    if start == 0:
        res = res +  ele
        start += 1
    else :
        res = res + " " + ele
        

print res