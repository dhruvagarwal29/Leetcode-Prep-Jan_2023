# Pair with Target Sum

# Given an array of sorted numbers and a target sum,
#  find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two
#  numbers (i.e. the pair) such that they add up to the given target.

def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == target:
            return left, right
        
        if arr[left] + arr[right] > target:
            right -=1 
        else:
            left +=1 
    
    return -1,-1

if __name__ == "__main__":
    arr= [1, 2, 3, 4, 6]
    target = 6

    i,j = two_sum(arr, target)

    print([i,j])