import numpy as np

#example 

board=[[0,0,0,8,0,7,4,0,0],
      [0,5,8,0,4,1,0,0,0],
      [7,0,0,0,0,0,0,0,2],
      [5,3,2,6,0,8,9,4,0],
      [4,8,0,1,2,9,3,7,0],
      [0,0,0,0,5,0,2,6,0],
      [0,2,7,9,0,0,0,0,4],
      [0,0,0,0,1,0,8,0,0],
      [8,6,0,0,0,0,5,0,9]]

             

init_board=board

#now, creating a function that determines whether a move is considered valid or not

def check_move(grid,row,col,num):
    
    #the following 2 loops check if a number lies in the column or row that it belongs to
    
    for i in range(9):
        if grid[row][i]==num:
            return False
    for j in range(9):
        if grid[j][col]==num:
            return False
        
    #the following code checks if the number lies in the 3*3 grid it belongs to
    
    row=row-row%3
    col=col-col%3
    for i in range(3):
        for j in range(3):
            if grid[row+i][col+j]==num:
                return False
    return True

#the function below solves the sudoku puzzle using recursion and backtracking

def solve_puzzle(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                for num in range(1,10):
                    if check_move(board,i,j,num):
                        board[i][j]=num
                        solve_puzzle(board)
                        board[i][j]=0
                return
    print(np.matrix(board))

#printing the initial grid and results
print(np.matrix(init_board),"\n")
print("solution to the given is: ","\n")
solve_puzzle(board)
