# leetcode 39 question 

# give the sequences whose sum is equal to target but here repeatation of elements are allowed 

# time complexity is O(2^n * k)
def combination_sum(arr, target, index, result, current):

    # base case 
    if index==len(arr):
        if target == 0:
            result.append(list(current))
            return
        else:
            return
        
    # now elements can be repeated so to take that into consideration in "take element" part 
    # we are not going to increase the index over here in recursion call 
    if arr[index] <= target:
        current.append(arr[index])
        combination_sum(arr, target - arr[index], index, result, current) # decrease the target 
        current.pop()
    # in not take part we are going to increase the index 
    combination_sum(arr, target, index+1, result, current)# target will be same as we are not picking 
    # here in the first call
    
    return result


if __name__=="__main__":
    arr= [2,3,5,7]
    target = 7

    print(combination_sum(arr, target, 0, [], []))