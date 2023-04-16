def NoughtsDeterminer(strArr):
    board_size = 3
    
    def get_row(row):
        row_start = row * board_size
        return strArr[row_start:row_start+board_size]
    
    def get_column(col):
        col_start = col % board_size
        return [strArr[col_start+i*board_size] for i in range(board_size)]
    
    def get_diagonal(diag):
        if diag == 0:
            return [strArr[i] for i in range(0, board_size**2, board_size+1)]
        elif diag == 1:
            return [strArr[i] for i in range(board_size-1, board_size**2-1, board_size-1)]
        else:
            return None
    
    def check_win(player):
        for i in range(board_size):
            if [player] * board_size == get_row(i):
                return i * board_size + get_row(i).index("-")
            elif [player] * board_size == get_column(i):
                return i + board_size * get_column(i).index("-")
        for i in range(2):
            if [player] * board_size == get_diagonal(i):
                return board_size*i + get_diagonal(i).index("-")
        return -1
    
    for player in ["X", "O"]:
        win_move = check_win(player)
        if win_move != -1:
            return win_move
    
    return -1


if __name__=="__main__":
    strArr = ["X","O","-","<>","-","O","-","<>","O","X","-"]

    print(NoughtsDeterminer(strArr))