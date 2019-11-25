

str = raw_input("Enter the string \n")
out = ""
print len(str)

def combination(start):
    global str,out
    for i in range(start,len(str)):
        out = out + str[i]
        print out
        if i < len(str):
            combination(i+1)
        out = out[0:len(out)-1]
        
combination(0)