numbers=["Indian, Institute, of, Technology, Patna"][0].split(",")
def longest_increasing_subsequence(numbers):
    tails = [0] * len(numbers)
    size = 0
    for x in numbers:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size

def get_stream_of_data():
    while True:
        print("ENter the text")
        _in = input()
        yield _in.split()


master_string_list = []
while True:
    g = get_stream_of_data() # consume from topic if kafka is the producer instead of generator
    _li = next(g)
    master_string_list.extend(_li)
    print(master_string_list)
    print("The length of longest increasing subesequence so far is {}".format(longest_increasing_subsequence(master_string_list)))
