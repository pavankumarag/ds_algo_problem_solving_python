def binary_search(a, ele, occurence="default"):
    '''
    This is a extended binay search program which covers the following things
    1. to search for element in a duplicate list 
    2. to search first or last occurence in a list having duplicate element
    3. guard rails when empty list is passed
    4. guatd rails when anything other than list data type is passed
    The code is self explanatory in a way of calculating mid and search till low <= high.
    Please note the time complexities of first and last occurence calculation is more than O(logn) as we need to search in extended left/right list
    However for default occurence the time complexity if O(logn)
    '''
    if len(a) <= 0:
        raise Exception("Its not possibel to search in empty list")
    if type(a) != list:
        raise Exception("This Binary search currently supports to search in list data type only")
    low = 0
    high = len(a) - 1
    index = -1
    while low <= high:
        mid = int((low + high) / 2)
        if a[mid] == ele:
            index = mid
            if occurence == "default":
                return index
            elif occurence == "first":
                high = mid -1
            elif occurence == "last":
                low = mid + 1
        elif ele > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return index

def binary_search_rec(a, low, high, ele, ri=-1, occurence="default"):
    '''
    This is the recursive implementation of binary search with first and last occurence support
    '''
    if low <= high:
        mid = int((low + high)/2)
        if a[mid] == ele:
            if occurence == "default":
                return mid
            elif occurence == "first": # then search in left list
                return binary_search_rec(a, low, mid-1, ele, ri=mid, occurence=occurence)
            elif occurence == "last": # then search in right list
                return binary_search_rec(a, mid+1, high, ele, ri=mid, occurence=occurence)
        elif ele > a[mid]:
            return binary_search_rec(a, mid+1, high, ele, ri, occurence)
        else:
            return binary_search_rec(a, low, mid-1, ele, ri, occurence)
    else:
        return ri

if __name__=="__main__":
    def execution():
        #Execution details
        length = int(input("Enter the length of the list\n"))
        _elements = input("Enter the elements of the list\n")
        list_str_elements = _elements.split(' ')
        list_int_elements = [int(ele) for ele in list_str_elements]
        print(list_int_elements)
        queries = int(input("Enter the number fo queries to be executed\n"))
        for _ in range(queries):
            search_element = int(input("Enter the search element\n"))
            index = binary_search(list_int_elements, search_element)
            if index != -1 :
                print("Element found at {} index".format(index))
            else:
                print("Element NOT found {}".format(index))
    
    def test_case1():
        '''
        Test case 1 - Printing the last occurence in a list having duplicate elements
        '''
        a = [3,8,12,12,12,12,14,14,16]
        ele = 14
        print(binary_search(a, ele, occurence="last"))
    def test_case2():
        '''
        Test case 2 - Search for a non existent element
        '''
        a = [3,8,12,12,12,12,14,14,16]
        ele = 13
        print(binary_search(a, ele))
    
    def test_case3():
        '''
        Test case 2 - Corner case passing an empty list
        '''
        a = []
        ele = 13
        print(binary_search(a, ele))
    execution()
    test_case1()
    test_case2()
    test_case3()
