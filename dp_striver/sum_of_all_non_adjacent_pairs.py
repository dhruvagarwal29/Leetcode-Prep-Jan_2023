# lets try out all the subsequences with the given constraint, pick the one with the maximum sum 

# recursion first 
# pick and non pick technique for the recurison 

def sum_of_non_adjacent_pairs_recursion(index, arr):
    # time complexity will be <= O(2^n)

    # base case 
    if index == 0:
        return arr[index]
    
    if index < 0:
        return 0
    
    # pick case but rememeber not 2 adjacents can be together

    pick = arr[index] + sum_of_non_adjacent_pairs_recursion(index -2 , arr) # index -2 as no adjacent can be together

    # not pick will start from index -1 as we are not picking index so we can go one step back in this

    not_pick = 0 + sum_of_non_adjacent_pairs_recursion(index - 1, arr)

    return max(pick, not_pick)

# memoization
def sum_of_non_adjacent_pairs_memoization(index, arr, dp):
    # base case 
    if index ==0:
        return arr[index]
    
    if index < 0:
        return 0
    
    if dp[index] != -1:
        return dp[index]
    
    pick = arr[index] + sum_of_non_adjacent_pairs_memoization(index -2 , arr, dp)

    not_pick = 0 + sum_of_non_adjacent_pairs_memoization(index - 1, arr, dp)

    dp[index] = max(pick, not_pick)

    return dp[-1]

# tabulation 

def sum_of_non_adjacent_pairs_tabulation(index, arr):

    # define the dp array 

    dp = [0] * len(arr) 
    # base case 
    dp[0] = arr[0]
    
    # if index < 0:
    #     return 0
    
    for i in range(1, index):
    
        pick = arr[i] 
        
        if i > 1:

            pick += dp[i-2]

        not_pick = 0 + dp[i-1]

        dp[i] = max(pick, not_pick)

    return dp

if __name__=="__main__":

    arr = [1 , 2, 9] 
    index = len(arr) - 1
    print(sum_of_non_adjacent_pairs_recursion(index, arr))
    dp = [-1] * len(arr)
    print(sum_of_non_adjacent_pairs_memoization(index, arr, dp))
    print(sum_of_non_adjacent_pairs_tabulation(index, arr))
