#Number of queens
num=8

#chessboard
#NxN matrix with all elements 0
board = [[0]*num for i in range(num)]

def column_row(i, j):
    #checking if there is a queen in row or column
    for k in range(0,num):
        if board[i][k]==1 or board[k][j]==1:
            return True
    #checking diagonals
    for k in range(0,num):
        for l in range(0,num):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def N_queen(n):
    #if n is 0, solution found
    if n==0:
        return True
    for i in range(0,num):
        for j in range(0,num):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(column_row(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                #recursion
                #wether we can put the next queen with this arrangment or not
                if N_queen(n-1)==True:
                    return True
                board[i][j] = 0

    return False

N_queen(num)
for i in board:
    print (i)
