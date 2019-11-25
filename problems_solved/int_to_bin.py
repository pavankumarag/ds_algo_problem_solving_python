num = int(raw_input("Enter the integer"))
bin,rem,rev,cmp =0,0,0,0
pow = 1

while num > 0:
    rem = num % 2
    bin = bin + rem*pow
    pow = pow * 10
    num = num/2 

print bin
cmp = bin

while bin > 0:
    rem = bin % 10
    rev = rev * 10 + rem
    bin = bin/10 

print rev

if cmp == rev :
    print "The binary representation of the given number is palindrome"