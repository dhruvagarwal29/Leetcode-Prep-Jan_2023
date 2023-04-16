# Given a set of positive numbers, find if we can partition
# it into two subsets such that the sum of elements in both subsets is equal.

# using backtrack here 

# this solution is correct but time limit got exceeded in this

def find_subset(arr):
    s = sum(arr)
    result = []
    if s%2 != 0:
        return False
    target = s //2 
    for i in range(len(arr)):
        current_arr = [arr[i]]
        remaining_arr = arr[i+1:]
        backtrack(current_arr, remaining_arr, target, result)
    print(result)
    if len(result) > 0: 
        return True

def backtrack(current_arr, remaining_arr, target, result):
    if sum(current_arr) == target:
        result.append(list(current_arr))
        return

    if sum(current_arr) > target:
        return 
    
    for j in range(len(remaining_arr)):
        ch = remaining_arr[j]
        current_arr.append(ch)
        backtrack(current_arr, remaining_arr[j+1:], target, result)
        current_arr.pop()

if __name__=="__main__":
    arr = [1,2,3,4]
    print(find_subset(arr))
