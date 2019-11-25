


def permute():
    global out,str
    global used
    if len(out) == len(str):
        print out
        return
    for i in range(len(str)):
        try:
            if used[i] == 1 :
                continue
        except:
            pass
        out = out + str[i]
        used[i] = 1
        permute()
        used[i] = 0
        out = out[0:len(out)-1] 
        

str = raw_input("Enter the string\n")
out = ""
used = dict()

permute()
