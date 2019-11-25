def convert_to_binary(number):
    binary = list()
    i=0
    while number > 0 :
        binary.append(str(number%2))
        number=number/2
        i=i+1
    binary.reverse()
    return "".join(binary)

def sum_bin(a, b):
    rules = {('0', '0'):(0,0),
             ('0', '1'):(1,0),
             ('1', '0'):(1,0),
             ('1', '1'):(0,1)
            }
    carry = 0
    sum = 0
    result = ""
    for x,y in zip(reversed(a),reversed(b)):
        sum = rules[(x,y)][0]
        if carry:
            sum = rules[(str(sum), str(carry))][0]
        result += str(sum)
        carry = rules[(x,y)][1]

    if carry:
        result += str(1)
    print result 
    return result[::-1]


a= 4
b= 5
a_bin = convert_to_binary(a)
b_bin = convert_to_binary(b)
if (len(a_bin) > len(b_bin)):
    b_bin = b_bin.rjust(len(a_bin),'0')
elif (len(a_bin) < len(b_bin)):
    a_bin = a_bin.rjust(len(b_bin),'0')
    
print sum_bin(a_bin, b_bin)
