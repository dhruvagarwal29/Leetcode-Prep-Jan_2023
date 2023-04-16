# You’ve been provided with the nums integer array, representing the series of squares.
#  The player starts at the first index and, following the rules of the game, tries to reach the last index.

#Assume player can reach the last index, your function returns min no of jumps required; otherwise, it returns FALSE.


def min_jump(nums):
    farthest_jump = 0
    current_jump = 0 
    count_of_jumps= 0

    for i in range(len(nums)-1):
        farthest_jump = max(farthest_jump, i + nums[i])
        if i == current_jump:
            count_of_jumps+=1
            current_jump = farthest_jump
    return count_of_jumps

    
if __name__ == "__main__":

    nums = [2,3,1,1,4]
    nums1 = [2,1,1,1,4]
    arr= [1,2,3,4,5]
    array = [2, 0, 1, 1, 2, 3, 6]

    print(min_jump(nums))
