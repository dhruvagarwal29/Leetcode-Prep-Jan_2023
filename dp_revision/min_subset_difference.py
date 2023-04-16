# Given a set of positive numbers, partition the set into two subsets with minimum 
# difference between their subset sums.


# brute force using recursion


def min_diff(arr, current_index, sum1, sum2):

    # base case

    if current_index == len(arr):
        return abs(sum1 - sum2)
    
    # now calculate 

    diff1 = min_diff(arr, current_index+1, sum1 + arr[current_index], sum2)
    print(diff1)
    diff2 = min_diff(arr, current_index+1, sum1 , sum2+ arr[current_index])

    return min( diff1, diff2)


if __name__=="__main__":

    arr = [1,2,3,9]

    current_index = 0
    sum1 = 0
    sum2 = 0

    print(min_diff(arr, current_index, sum1, sum2))