# Given a set of positive numbers, find if we can partition
# it into two subsets such that the sum of elements in both subsets is equal.

# using dp so TLE will not occur
import pprint as p
def find_subset(arr):
    s = sum(arr)
    result = []
    if s%2 != 0:    
        return False
    target = s //2  # THIS IS GOING TO BE MY COLUMNS 
    # AND ARR IS MY ROWS 

    dp = [[0 for i in range(target + 1)] for j in range(len(arr) + 1)]
    #print(dp)
    for i in range(1, len(arr) + 1):# rows loop 
        for j in range(1, target + 1): # columns loop 
            if j >= arr[i-1]:
                previous_value = dp[i-1][j] 

                # previous value shows the value hold by previous row for the same target value 
                # new value shows the value hold current arr value we have used arr[i-1]
                # as arr has 4 elements only and we increase the size dp to 4 
                # so new value is addition of current arr value and previous value of dp
                # dp[previous row][ current_target_value - current_array value]
                
                new_value = arr[i-1] + dp[i-1][j - arr[i-1]]
                dp[i][j] = max(previous_value, new_value)
            else:
                dp[i][j] = dp[i-1][j]

    p.pprint(dp)
    return dp[-1][-1] == target

if __name__=="__main__":
    arr = [1,2,3,4]
    print(find_subset(arr))
