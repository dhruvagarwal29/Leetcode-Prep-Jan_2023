# If the player can reach the last index, your function returns TRUE; otherwise, it returns FALSE.

def jump_game(arr):
    # make the target index at last index of the array and we will traverse this loop in reverse 
    # if previous element is able to reach to the target index then we will put the target index as the 
    # current index 
    target_index = len(arr)-1

    for i in range(len(arr)-2,-1,-1):
        # here if we see that if we are able to reach the target index by adding the current index and 
        # value in current index then we will shift the target index to the current index and make that 
        # target...now if target index is equal to 0 then it means it reaches the end and has path 
        if target_index <= i+arr[i]:
            target_index = i 

    if target_index ==0:
        return True
    else:
        return False

if __name__=="__main__":
    arr= [2,3,1,1,4]
    print(jump_game(arr))