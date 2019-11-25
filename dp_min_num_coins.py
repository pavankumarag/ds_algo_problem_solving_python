#Q: What is the minimum number of coins of values v1,v1,v3...vn required to amount a total of V?
# You may use a denomination more than once
# V = the value we want, v=the list of available denomenations

#naive recursion is a bad way
def coinsChange(V,v):
    dpTable = [float("inf")]*(V+1)
    dpTable[0] = 0
    for i in xrange(1,V+1):
            for vi in v:
                    if (i - vi) >= 0:
                            dpTable[i] = min(dpTable[i],1+dpTable[i-vi])
    return dpTable[V]

#solving using memoization way
def coinsChange_mem(V,v):
    memo = {}
    def Change(V):
            if V in memo:
                    return memo[V]
            if V == 0:
                    return 0
            if V < 0:
                    return float("inf")
            memo[V] = min([1+Change(V-vi) for vi in v])
            return memo[V]
    return Change(V)

if "__name__" == "main":
  print coinsChange(11, [1,2,5]) #Prints 3