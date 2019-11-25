'''
ProbLem Write an efficient function that deletes characters from an ASCII string. Use the prototype
string removeChars( string str, string remove );
where any character existing in remove must be deleted from str. 
For example, givenastrof"Battle of the Vowels: Hawaii vs. Grozny"andaremoveof "aeiou",
thefunctionshouldtransformstrto“Bttl f th Vwls: Hw vs. Grzny”. Justify any design decisions you make, and discuss the efficiency of your solution.

1. Shift 
2. Iterate every character in rem with every character in str, so this takes O(nm)

'''

str = raw_input("Enter the string")
rem = raw_input("Enter the characters to be removed")

new = ""
d = {}

for ch in rem :
    d[ch] = 1

print d
dst = 0
for ch in str:
    if ch in d.keys():
        if d[ch] != 1 :
            new += ch     
    else:
        new += ch
                    
print new
    



