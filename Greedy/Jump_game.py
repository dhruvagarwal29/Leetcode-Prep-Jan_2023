# You’ve been provided with the nums integer array, representing the series of squares.
#  The player starts at the first index and, following the rules of the game, tries to reach the last index.

#If the player can reach the last index, your function returns TRUE; otherwise, it returns FALSE.



def jump_game(nums):
    # set the target as last element 
    target = len(nums) - 1

    for index in range(len(nums)-2, -1, -1):
        if index + nums[index]>= target:
            target = index 
    

    if target==0:
        return True
    else:
        return False
    
if __name__ == "__main__":

    nums = [2,3,1,1,5]

    print(jump_game(nums))
