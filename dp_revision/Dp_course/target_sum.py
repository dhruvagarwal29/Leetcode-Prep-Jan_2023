# Given an array of positive integers arr and a target T, 
#build an expression using these numbers by inserting a  + or - and count the total expression

def target_sum_naive(arr, target, current_index, sum):
    # base case if current index reached len(arr)
    if current_index ==len(arr):
        
        if sum == target:
            return 1
        else:
            return 0
        
    # take + 
    positive_expressions = target_sum_naive(arr, target, current_index +1, sum+arr[current_index])

    # take -
    negative_expressions = target_sum_naive(arr, target, current_index +1, sum-arr[current_index])
          
    return positive_expressions + negative_expressions
    
    

if __name__=="__main__":
    arr= [1,1]
    target = 0
    current_index = 0
    sum = 0
    print(target_sum_naive(arr, target, current_index,sum))
 