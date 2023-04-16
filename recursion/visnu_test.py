# test 
# noughts determiner 

def NoughtsDeterminer(strArr):
    BOARD_SIZE = 3
    ROW_SEPARATOR = '<>'
    EMPTY_CELL = '-'
    PLAYERS = ['O', 'X']
    board = [row.split() for row in ''.join(strArr).split(ROW_SEPARATOR)]
    board_size = len(board)

    def get_row(index):
        return board[index // BOARD_SIZE]

    def get_column(index):
        return [board[i][index % BOARD_SIZE] for i in range(board_size)]

    def get_diagonal(index):
        if index == 0:
            return [board[i][i] for i in range(board_size)]
        elif index == 2:
            return [board[i][board_size - 1 - i] for i in range(board_size)]
        else:
            return []

    for i, cell in enumerate(''.join(strArr)):
        if cell == EMPTY_CELL:
            for player in PLAYERS:
                if [player] * BOARD_SIZE in (get_row(i), get_column(i), get_diagonal(i)):
                    return i

    return -1


if __name__=="__main__":
    strArr = ["X","O","-","<>","-","O","-","<>","O","X","-"]

    print(NoughtsDeterminer(strArr))