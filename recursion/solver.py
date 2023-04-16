# class Solution:
#     def solve_sudoku_helper(self, board):
#         for row in range(len(board)):
#             for col in range(len(board[0])):
#                 if board[row][col] == '.':
#                     for char in range(1, 10):
#                         if self.is_valid(board, row, col, str(char)):
#                             board[row][col] = str(char)
#                             if self.solve_sudoku_helper(board):
#                                 return True
#                             board[row][col] = '.'
#                     return False
#         return True

#     def is_valid(self, board, row, col, char):
#         for i in range(9):
#             if board[row][i] == char or board[i][col] == char:
#                 return False
#             sub_box_row = 3 * (row // 3) + i // 3
#             sub_box_col = 3 * (col // 3) + i % 3
#             if board[sub_box_row][sub_box_col] == char:
#                 return False
#         return True


def solve_sudoku_helper(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '.':
                for char in range(1, 10):
                    if is_valid(board, row, col, str(char)):
                        board[row][col] = str(char)
                        if solve_sudoku_helper(board):
                            return True
                        else:
                            board[row][col] = '.'
                return False
    return True

def is_valid(board, row, col, char):
    for i in range(9):
        if board[row][i] == char or board[i][col] == char:
            return False
        sub_box_row = 3 * (row // 3) + i // 3
        sub_box_col = 3 * (col // 3) + i % 3
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
    #sol = Solution()
    solve_sudoku_helper(board)
    print(board)
    