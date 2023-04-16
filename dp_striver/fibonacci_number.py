# calcualte the fibonacci number 
# writing recursion 

def fibonacci_number_recursive(num):
    if num <=1:
        return num
    
    return fibonacci_number_recursive(num - 1) + fibonacci_number_recursive(num - 2)

# now using dp 

def fibonacci_number_dp(num):
    # declare th dp array of num + 1 size as 0 will also be there 
    dp = [-1] * (num + 1)
    #print(dp)
    # base case 
    if num <= 1:
        return num 
    
    # if number is not equal to -1 then return the position of num from dp array
    if dp[num] != -1:
        return dp[num]
    # this is a better solution but needs recursion space so more space complexity
    dp[num] = fibonacci_number_dp(num - 1) + fibonacci_number_dp(num - 2)
    #print(dp)
    return dp[num]

def fibonacci_number_dp_tabulation(num):
    # this is better than the recursion one using dp
    dp = [-1] * (num + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, num+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[num]

def fibonacci_number_dp_space_optimized(num):
    # here we are using variable instead of the dp array 
    # time complexity is O(n), space complexity is O(1)
    prev = 1 # second element dp[1]
    prev2 = 0 # first element dp[0]

    for i in range(2,num+1):
        current = prev2 + prev
        # dp[i] = dp[i-2] + dp[i-1]
        # here we are transferring the values to avoid dp 
        # ur dp[i-2] will become dp[i-1] ie prev2 = prev
        prev2 = prev 
        # and giving dp[i-1] to the value of dp[i] ie prev = current
        prev = current

    return prev
if __name__=="__main__":
    num = 5
    print(fibonacci_number_recursive(num))
    print(fibonacci_number_dp(num))
    print(fibonacci_number_dp_tabulation(num))
    print(fibonacci_number_dp_space_optimized(num))