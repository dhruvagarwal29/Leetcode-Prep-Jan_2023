# find the sum in ordeer of all the subsets of the array 
def subset_sums(arr, index, sum, result):
    # base case
    if index == len(arr):
        result.append(sum)
        return

    # pick the element "take"
    subset_sums(arr, index+1, sum+arr[index], result)

    # not pick the element "not take"
    subset_sums(arr, index+1, sum, result)

    return sorted(result)

if __name__=="__main__":
    arr = [3,1,2]
    index = 0
    sum = 0 
    result = []
    print(subset_sums(arr, index, sum, result))

    