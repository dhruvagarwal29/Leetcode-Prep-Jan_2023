# Given a set of positive numbers, determine if a 
#subset exists whose sum is equal to a given number ‘S’.

# using dp here 
import pprint as pp
def sum_subset(arr, target):
    # target is my columns 
    # arr is my rows 

    dp = [[0 for i in range(target + 1)] for j in range(len(arr)+1)]

    # loop for rows 
    for i in range(len(arr) +1 ):
        for j in range(target + 1): # loop for columns
            if j >= arr[i-1]:
                dp[i][j]= max(arr[i-1] + dp[i-1][j - arr[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    #pp.pprint(dp)
    return dp[-1][-1] == target          

if __name__=="__main__":
    print(sum_subset(arr = [1,2,3,7], target = 6))
    print(sum_subset(arr = [1,2,7,1,5], target = 10))
    print(sum_subset(arr = [1,3,4,8], target = 6))

