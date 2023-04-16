# match stick square

def match_stick_square(array):
    # first side will be the total sum of the numbers in array divided by 4 
    one_side = sum(array) // 4 

    if one_side * 4 != sum(array):
        return False
    
    


if __name__ == "__main__":
    arr = [1,1,2,2,2]

    print(match_stick_square(arr))