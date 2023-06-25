# why greedy solu will not work here ? 

# we cant see all the possible ways in greedy so we have to use recursion here 

# try all possible ways---write recursion

# Steps - 1) express the problem in terms of index 
# 2) Perform all stuff on this index 
# 3) Take the minimal of all stuffs 



def frog_jump_recursive(index, arr): 
    # this is a recursive solution it will give TLE
    
    if index==0:
        return 0
    
    one_step = frog_jump_recursive(index-1, arr) + abs(arr[index] - arr[index-1])
    two_step = float('Inf')

    if index>1:
        
        two_step = frog_jump_recursive(index-2,arr) + abs(arr[index] - arr[index-2])

    return min(one_step, two_step)

def frog_jump_dp_array(index, arr, dp):

    if index==0:
        return 0
    
    # if dp[index] is not equals to -1 then return dp[index]
    if dp[index] != -1:
        return dp[index]
    
    one_step = frog_jump_dp_array(index-1, arr,dp) + abs(arr[index] - arr[index-1])

    two_step = float('Inf')

    if index>1:
        
        two_step = frog_jump_dp_array(index-2,arr,dp) + abs(arr[index] - arr[index-2])

    dp[index] = min(one_step, two_step)
    return dp[index]


def frog_jump_tabulation(index, arr):

    # initialize dp array 
    dp = [-1] * (len(arr)) # initialize the dp 
    dp[0] = 0  # base case 

   
    for i in range(1,len(arr)):   # looping till 1 to n-1 
        one_step = dp[i-1] + abs(arr[i] - arr[i-1]) # first step
        two_step = float('Inf')

        if i>1: # as we cant go back  two steps from stair 1 
            two_step = dp[i-2] + abs(arr[i] - arr[i-2])

        dp[i] = min(one_step, two_step) # putting the min value of one and two step in dp array
        
    return dp[-1]


def frog_jump_space_optimized(index, arr):
    # two variables for making the swap
    prev = 0  
    prev2 = 0
   
    for i in range(1,len(arr)):   # looping till 1 to n-1 
        one_step = prev + abs(arr[i] - arr[i-1]) # first step
        two_step = float('Inf')

        if i>1: # as we cant go back  two steps from stair 1 
            two_step = prev2 + abs(arr[i] - arr[i-2])

        curri = min(one_step, two_step) # putting the min value of one and two step in dp array
        
        # interchange the values 
        prev2 = prev
        prev = curri 
    return prev

if __name__=="__main__":
    arr = [10,20,30,10]
    # i have given index as len(arr)-1 as question starts from 0 indexing.
    print(frog_jump_recursive(len(arr)-1,arr)) # recursive way
    # dp array 
    dp = [-1] * (len(arr)+1)
    print(frog_jump_dp_array(len(arr)-1,arr, dp))
    print(frog_jump_tabulation(len(arr), arr))
    print(frog_jump_space_optimized(len(arr), arr))