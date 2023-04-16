# count all the subsequences that equal to sum k

def count_subsequences(arr, target, index, sum):

    # TIME COMPLEXITY IS O(2^N) SOME OF IT CAN BE SAVED BY GIVING ONE CONDITON BUT ONLY WOKRS 
    # FOR POSITIVE ARRAY THAT IS "IF  SUM > TARGET THEN ALSO RETURN 0 "
    
    # base case 

    if sum > target:
        return 0    
    if index == len(arr):
        if sum == target:
            return 1
        else:
            return 0
        
    sum += arr[index] 
    left = count_subsequences(arr, target, index+1, sum)  # CHECK THE SUBSEQUENCES WITH TAKING ELEMENT
    sum -= arr[index]
    right = count_subsequences(arr, target, index+1, sum)# CHECK THE SUBSEQUENCES WITH NOT TAKING ELEMENT

    return left + right # RETURN THE ADDITON OF THE BOTH


if __name__=="__main__":
    arr = [1,2,1]
    target = 2
    sum = 0
    index = 0
    print(count_subsequences(arr, target, index, sum))

