# we have to check if we can place "x" or "o" in a position where we can make the user win 

def noughts_determiner(board):
    # print the board intoi 3*3 
    j=0
    for i in range(len(board)):
        if board[i] == "<>":
            print(board[j:i])
            j= i+1
    
    print(board[j:i+1])

    for i in range(len(board)):
        symbol = board[i]
        if symbol == "-":
            if (horizontal_check(board, i) or 
                vertical_check(board, i) or
                diagonal_check(board, i)):
                return i
    
    return -1


def horizontal_check(board, current_index):
    X_count = 0
    O_count = 0

    while current_index -3 > 0:
        current_index-=3 # bring the index to the 0 value 

    if current_index < 3:
        for i in range(3):
            if board[i] =="X":
                X_count += 1
            elif board[i] == "O":
                O_count += 1

    elif current_index > 3 and current_index < 7: 
        for i in range(4,7):
            if board[i] =="X":
                X_count += 1
            elif board[i] == "O":
                O_count += 1

    else:
        for i in range(8,10):
            if board[i] =="X":
                X_count += 1
            elif board[i] == "O":
                O_count += 1

    if X_count == 2:
        return True
    elif O_count == 2:
        return True
    else:
        return False
    

def vertical_check(board, current_index):
    X_count = 0
    O_count = 0

    while current_index -3 > 0:
        current_index -= 3

    for i in range(2):
        if board[current_index] == "X":
            X_count +=1
        elif board[current_index] == "O":
            O_count += 1
        
        current_index += 3 # to check for next row
    
    if X_count == 2:
        return True
    elif O_count == 2:
        return True 
    else:
        return False

def diagonal_check(board, current_index):
    right_diagonal = [0,5,10]
    left_diagonal = [2, 5, 8]

    X_count = 0
    O_count = 0

    if current_index in right_diagonal:
        for i in right_diagonal:
            if board[i] =="X":
                X_count +=1
            elif board[i] == "O":
                O_count += 1
    elif current_index in left_diagonal:
        for i in left_diagonal:
            if board[i] =="X":
                X_count +=1
            elif board[i] == "O":
                O_count += 1

    if X_count == 2:
        return True
    elif O_count == 2:
        return True 
    else:
        return False

if __name__=="__main__":
    strArr = ["X","O","-","<>","-","O","-","<>","O","X","-"]

    print(noughts_determiner(strArr))