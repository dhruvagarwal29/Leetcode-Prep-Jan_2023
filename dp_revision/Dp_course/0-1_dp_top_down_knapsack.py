# now using dp to solve the 0-1 knapsack problem 

# top down is an iterative way of using the dp method with the help of an array



def top_down(weights, values, capacity, last_index):
    # last index is len of weights
    if last_index == 0 or capacity ==0:
        return 0
    
    # make dp array of the capacity and weights and fill them accordingly to the profits 

    dp = [[0 for column in range(capacity+1)] for row in range(len(weights) + 1)]

    # dp is a 2D array where columns belongs to capacity and rows belongs to the weights given
    # i is the current weight from weights array
    # j is the capacity from range of the capacity


    for i in range(1, last_index+1):
        for j in range(capacity+1):

            if j >= weights[i-1]:

                dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j - weights[i-1]])
                # here we are saying dp[wei][cap] is either the previous weight cap value or the 

            # else:
            #     dp[i][j] = dp[i-1][j]
            
    print(dp)

    return dp[-1][-1]


if __name__== "__main__":

    weights = [3, 2, 1, 5]
    values = [4, 5, 10, 8]
    capacity = 5
    last_index = len(weights)
    
    print(top_down(weights, values, capacity, last_index))