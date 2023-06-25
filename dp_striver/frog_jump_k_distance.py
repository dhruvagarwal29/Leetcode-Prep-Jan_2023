# this is the sequel of the frog jump question where we are asked to have K no. of jumps 

def frog_jump_recursive(index, arr, k): 
    # this is a recursive solution it will give TLE
    
    if index==0:
        return 0
    
    min_steps = float('Inf')

    for i in range(1,k+1):
        if (index - i >= 0):
            jump = frog_jump_recursive(index - i, arr, k) + abs(arr[index] - arr[index - i])
            min_steps = min(min_steps, jump)
        
    return min_steps

def frog_jump_tabulation(index, arr, k):
    dp = [0] * (index)

    for i in range(1, index):
        min_steps =  float('Inf')

        # k steps loop 
        for j in range(1, k+1):
            if i-j >= 0:
                jump = dp[i-j] + abs(arr[index] - arr[index - j])
                min_steps = min(jump, min_steps)

        dp[i] = min_steps
    
    return dp[index-1]
if __name__=="__main__":
    arr = [10,20,30,10]
    k=2
    index = len(arr)-1
    # i have given index as len(arr)-1 as question starts from 0 indexing.
    print(frog_jump_recursive(index, arr, k)) # recursive way
    print(frog_jump_tabulation(index, arr, k))