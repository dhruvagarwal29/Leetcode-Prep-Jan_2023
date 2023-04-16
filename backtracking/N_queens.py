# Given a chessboard of size n \times nn×n, determine how many ways n
# n queens can be placed on the board, such that no two queens attack each other.

# A queen can move horizontally, vertically, and diagonally on a chessboard. One queen can be attacked by another queen if both share the same row, column, or diagonal.
from pprint import pprint




def is_valid_move(proposed_row, proposed_col, solution):
    for i in range(0, proposed_row):
        old_row = i
        old_col = solution[i]
        diagonal_offset = proposed_row - old_row
        if (old_col == proposed_col or
            old_col == proposed_col - diagonal_offset or
                old_col == proposed_col + diagonal_offset):
            return False
            
    return True


def solve_n_queens_recusion(n, solution, row, result):

    if row==n:
        result.append(solution)
        return
    
    for i in range(0, n):
        valid = is_valid_move(row, i, solution)
        if valid:
            solution[row] = i
            solve_n_queens_recusion(n, solution, row+1, result)



# funtion to solve n queens
def solve_n_queens(n):
    result = []
    solution = [-1] * n 
    solve_n_queens_recusion(n, solution, 0, result)
    return len(result)



if __name__ == "__main__":
    
    n = 4

    res = solve_n_queens(n)

    pprint(res)


