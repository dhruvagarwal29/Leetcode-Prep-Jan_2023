# count ways to reach n stairs 
# why this is dp :?>

# 1) count the total no of ways 
# 2) try all possible ways then apply recursion 
# first step is recursion 

# shortcut dp
'''
1) try to represent the problem in terms of index 
2) Do all possible stuffs on that index according to problem statement 
3) If ques says count all ways then sum up all the stuffs 
   If ques says find min. then take min of all stuffs and accordingly for maximum
'''

# this is same as fibonacci number

def count_n_stairs_ways_recursive(num):

    if num == 0 or num == 1:
        return 1
    
    # so we have the index that is num and we can take 1 jump or 2 jump at a time 

    one_step_jump = count_n_stairs_ways_recursive(num - 1)
    two_step_jump = count_n_stairs_ways_recursive(num - 2)

    return one_step_jump + two_step_jump

def count_n_stairs_ways_dp(num):
    dp = [-1] * (num + 1)

    if num == 0 or num == 1:
        return 1 # as we can one jump from 1 to 0, ie one jump 
    
    if dp[num] != -1:

        return dp[num]
    
    dp[num] = count_n_stairs_ways_dp(num-1) + count_n_stairs_ways_dp(num-2)

    return dp[num]

def count_n_stairs_ways_dp_tabulation(num):
    dp = [-1] * (num + 1)
    # now we are using 1D dp array 
    dp[0] = 1
    dp[1] = 1

    for i in range(2, num+1):
        dp[i] = dp[i-2] + dp[i-1]
    
    return dp[num]

def count_n_stairs_ways_dp_tabulation_memory_saved(num):
    # this is same as tabulation but we are going to use variables instead of dp array 

    prev2 = 1
    prev = 1

    for i in range(2, num+1):
        current = prev2 + prev
        prev2 = prev
        prev = current
    
    return prev


if __name__=="__main__":
    num = 3
    print(count_n_stairs_ways_recursive(num))
    print(count_n_stairs_ways_dp(num))
    print(count_n_stairs_ways_dp_tabulation(num))
    print(count_n_stairs_ways_dp_tabulation_memory_saved(num))

