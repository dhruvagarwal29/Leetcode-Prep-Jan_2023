def noughts_determiner(board):
    j = 0
    for i in range(len(board)):
        if board[i] == '<>':
            print(board[j:i])
            j = i+1

    print(board[j:i+1])

    for i in range(len(board)):
        char = board[i]
        if char == '-':
            if (check_horizontal(board, i) or 
                check_vertical(board, i)  or 
                check_diagonal(board, i)):
                return i 

    return -1 
        
def check_horizontal(board, curr_ix):
    x_count = 0 
    o_count = 0 

    while curr_ix - 3 > 0:
        curr_ix -= 3 

    if curr_ix < 3:
        for i in range(0,3):
            if board[i] == 'X':
                x_count +=1 
            elif board[i] == 'O':
                o_count += 1 

    elif curr_ix > 3 and curr_ix < 7:
        for i in range(4,7):
            if board[i] == 'X':
                x_count +=1 
            elif board[i] == 'O':
                o_count += 1 
    else:
        for i in range(8,10):
            if board[i] == 'X':
                x_count +=1 
            elif board[i] == 'O':
                o_count += 1 

    if x_count == 2:
        return True
    elif o_count == 2:
        return True
    else:
        return False

def check_vertical(board, curr_ix):

    x_count = 0 
    o_count = 0 

    while curr_ix - 3 > 0:
        curr_ix -= 3 

    for i in range(2):
        if board[curr_ix] == 'X':
            x_count += 1 
        elif board[curr_ix] == 'O':
            o_count += 1 

        curr_ix += 3 
    
    if x_count == 2:
        return True
    elif o_count == 2:
        return True
    else:
        return False

def check_diagonal(board, curr_ix):
    diag = [0,5,10]
    cross_diag = [2,5,8]

    x_count = 0 
    o_count = 0 

    if curr_ix in diag:
        for i in diag:
            if board[i] == 'X':
                x_count += 1 
            elif board[i] == 'O':
                o_count += 1 
    elif curr_ix in cross_diag:
        for i in cross_diag:
            if board[i] == 'X':
                x_count += 1 
            elif board[i] == 'O':
                o_count += 1 
    
    if x_count == 2:
        return True
    elif o_count == 2:
        return True
    else:
        return False

if __name__ == "__main__":
    i = noughts_determiner(
        # ['x','o', 'o', '<>', '-', 'o', '-', '<>', '-', 'x', '-']
        # ["x","-","o","<>","-","-","o","<>","-","-","x"]
        #["x","o","x","<>","-","o","o","<>","x","x","o"]
        ["X","O","-","<>","-","O","-","<>","O","X","-"]
    )
    print(i)
    