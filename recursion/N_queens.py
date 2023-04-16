# # best way is recursion as we have to generate all the possible patterns 
# import pprint as pp
def is_safe(row, column, board, n):

    # make duplicates of row and column 
    drow = row
    dcol = column

    # now check for the upper left diagonal "\"
    while row>=0 and column>=0:
        if board[row][column] =="Q":
            return False
        row -= 1
        column -= 1

    row = drow
    column = dcol
    # now check for the left column "<-"
    while column>=0:
        if board[row][column] =="Q":
            return False
        column -= 1

    row = drow
    column = dcol
    # now check for the lower left diagonal "/"
    while row<n and column>=0:
        if board[row][column] =="Q":
            return False
        row += 1
        column -= 1

    return True

def n_queens(board, column, n,ans):

    if column == n:
        ans.append(list(board))     
        return
    
    for row in range(0, n):
        # now check if the row and column are safe to place a queen here or not

        if (is_safe(row, column, board, n)):
            board[row]= board[row][:column] + "Q" + board[row][column+1:]
            n_queens(board, column+1, n, ans)
            board[row]= board[row][:column] + "." + board[row][column+1:]
    
    return ans
if __name__=="__main__":
    # have to make board of n * n size 
    n = 4
    column = 0
    ans = []
    board = ["." * n for i in range(n)]
    print(n_queens(board, column, n, []))
    




# class Solution:
#     def isSafe1(self, row, col, board, n):
#         # check upper element
#         duprow = row
#         dupcol = col
        
#         while row >= 0 and col >= 0:
#             if board[row][col] == 'Q':
#                 return False
#             row -= 1
#             col -= 1
        
#         col = dupcol
#         row = duprow
#         while col >= 0:
#             if board[row][col] == 'Q':
#                 return False
#             col -= 1
        
#         row = duprow
#         col = dupcol
#         while row < n and col >= 0:
#             if board[row][col] == 'Q':
#                 return False
#             row += 1
#             col -= 1
#         return True

#     def solve(self, col, board, ans, n):
#         if col == n:
#             ans.append(board.copy())
#             return
#         for row in range(n):
#             if self.isSafe1(row, col, board, n):
#                 board[row] = board[row][:col] + 'Q' + board[row][col + 1:]
#                 self.solve(col + 1, board, ans, n)
#                 board[row] = board[row][:col] + '.' + board[row][col + 1:]

#     def solveNQueens(self, n):
#         ans = []
#         board = ['.' * n for i in range(n)]
#         print(board)
#         self.solve(0, board, ans, n)
#         return ans

# if __name__ == "__main__":
#     n = 4 # we are taking 4*4 grid and 4 queens
#     obj = Solution()
#     ans = obj.solveNQueens(n)
#     for i in range(len(ans)):
#         print("Arrangement", i + 1)
#         for j in range(len(ans[0])):
#             print(ans[i][j])
#         print()
