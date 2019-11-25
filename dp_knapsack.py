from array import *

def knapsack(n,v,w,W):
		rows, cols = (n, W)
		t = [[0] * cols] * rows
    for j in range(0, W+1):
       t[0][j]=0
    for i in range(1,n+1):
        for j in range(0,W+1):
            if w[i]>j:
                t[i][j]=t[i - 1][j]
            else
                t[i, j] = max(t[i - 1][j], t[i - 1][j - w[i]]+v[i])
     return t[n][W]