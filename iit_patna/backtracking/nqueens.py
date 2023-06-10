num_of_solutions = 0

def printBoard(board):
    global num_of_solutions
    num_of_solutions += 1
    print("Solution number {}".format(num_of_solutions))
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print()
    print()

def isSafe(board, row, col):

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQ(board, col):
    if col == len(board):
        printBoard(board)
        return

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(N):

        if isSafe(board, i, col):
            
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recursively try to place rest of the queens
            if solveNQ(board, col + 1) == True:
                return True
                
            # backtracking
            board[i][col] = 0

    return False

def solve():
     #chessboard
    #NxN matrix with all elements 0
    board = [[0]*N for _ in range(N)]

    if solveNQ(board, 0) == False:
        print ("No Possible Solution exists further")
        return False

    return True

if __name__ == "__main__":
    print ("Enter the number of queens")
    N = int(input())
    solve()
    print("\nTotal number of solutions {}\n".format(num_of_solutions))