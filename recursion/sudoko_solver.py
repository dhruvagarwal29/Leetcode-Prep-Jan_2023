# solve the sudoko 
# 3 conditions of solving sudoko is 
'''
1) the digit 1-9 only appear once in every column 
2) the digit 1-9 only appear once in any row 
3) the digit 1-9 only appear once in any 3*3 matrix in the sudoko
'''


def solve_sudoko(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            # check for the condition if place (board[row][column] is empty)
            if board[row][col] == '.':
                for char in range(1, 10):
                    if is_valid(board, row, col, str(char)):
                        # if the board is valid then place the char 
                        board[row][col] = str(char)
                        # now if the board is true then return true
                        if solve_sudoko(board):
                            return True 
                        else:
                            # remove the char or replace the char to "."
                            board[row][col] = '.'
                return False                                    
    return True
                
def is_valid(board, row, column, char):
    for i in range(9):
        # FOR COLUMN CHECK IF CHAR IS PRESENT WE JUST NEED TO TRAVERSE COLUMNS 
        # ROW STAY SAME
        
        if board[row][i] == char:
            return False
        
        # for row check we need to fix the column else remains same
        
        if board[i][column] == char:
            return False 
        
        # now to check if char is present in 3*3 matrix 
        # so formula for row is ((3* row/3) + i/3)
        # formula for column is ((3* column/3) + i%3)
        sub_box_row = 3 * (row // 3) + i // 3
        sub_box_col = 3 * (column // 3) + i % 3
        if board[sub_box_row][sub_box_col] == char:
            return False
        
    return True

if __name__=="__main__":
    board = [["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."]
              ,[".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]
    
    print(solve_sudoko(board))
    print(board)
    