def convert_to_binary(number):
    binary = list()
    i=0
    while number > 0 :
        binary.append(str(number%2))
        number=number/2
        i=i+1
    binary.reverse()
    return "".join(binary)

for i in range(20,30):
    print i, convert_to_binary(i)
        