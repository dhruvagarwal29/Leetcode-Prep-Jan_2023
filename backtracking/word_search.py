# find the given word if it exists or not in the given grid

def word_search(grid, target_word):
    rows = len(grid) # no of rows
    columns = len(grid[0]) # no of columns
    if rows<1:
        return False
    if columns<1:
        return False
    
    for row in range(rows): 
        for column in range(columns):
            if depth_first_search(row, column, target_word, grid):
                return True
    return False
    

def depth_first_search(row, col, word, grid):
    if len(word) == 0:
        return True

    if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) \
            or grid[row][col].lower() != word[0].lower():
        return False    
    
    result = False
    grid[row][col] = '*'

    for rowOffset, columnOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        result = depth_first_search(row + rowOffset , col + columnOffset, word[1:], grid)

        if result:
            break

    grid[row][col] = word[0]

    return result


if __name__ =="__main__":
    input = [['E', 'D', 'X', 'I', 'W'],
              ['P', 'U', 'F', 'M', 'Q'],
              ['I', 'C', 'Q', 'R', 'F'],
              ['M', 'A', 'L', 'C', 'A'],
              ['J', 'T', 'I', 'V', 'E']]
              
    word =  "educative"


    

    print(word_search(input, word))

