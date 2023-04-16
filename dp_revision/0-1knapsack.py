#Given the weights and profits of ‘N’ items, we are asked to put these items in a 
# knapsack which has a capacity ‘C’. 
# The goal is to get the maximum profit out of the items in the knapsack.
#  Each item can only be selected once, as we don’t have multiple quantities of any item.
import pprint as p

def knapsack(profits, weights, capacity):

    # make a dp array columns as capacity, rows as weights

    dp = [[0 for i in range(capacity + 1)] for j in range(len(weights)+1)]

    # print(dp)

    for i in range(1,len(weights)+1):
        for j in range(1, capacity+1):
            profit1 = dp[i-1][j] # get the profit of previous weight
            profit2 = 0
            if j >= weights[i-1]:
                profit2 = profits[i-1] + dp[i-1][j-weights[i-1]]
            # now check which is max profit1 that is previous row profit for same capacity 
            # or the new profit which came after getting a new weight 
            dp[i][j] = max(profit1, profit2)
    p.pprint(dp)
    return dp[-1][-1]
            

if __name__=="__main__":
    profits = [4,5,3,7]
    weights = [2,3,1,4]
    capacity = 5
    print(knapsack(profits, weights, capacity))