'''ProbLem Write a function that reverses the order of the words in a string.
 For example, your function should transform the string
  "Do or do not, there is no try." to "try. no is there not, do or Do". 
  Assume that all words are space delim- ited and treat punctuation the same as letters.


'''
s = raw_input("Enter the space delimited sentence\n")

ls = s.split(" ")
output  = []
i=0

print ls,len(ls)
for ele in range((len(ls)-1),-1,-1):
    output.append(ls[ele])
    i += 1
res = ""
for ele in output:
    res = res + " " + ele

print res
    
    