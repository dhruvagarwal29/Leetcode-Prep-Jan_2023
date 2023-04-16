# subset sums 2 # brute force is use 2^n solution and use set in it to remove duplicates 

# but we can also remove duplicates here also in recursion 

# WRITE A RECURSION IN SUCH WAY THAT IT WILL NOT CARRY DUPLICATES IN SUBSETS
def subset_sum_2(arr, index, result, current):
    result.append(list(current))

    for i in range(index, len(arr)):

        if i> index and arr[i] == arr[i-1]:
            continue
        current.append(arr[i])
        subset_sum_2(arr, i+1, result, current)
        current.pop()

    return result



if __name__=="__main__":
    arr  = [ 1, 2, 2]
    result = []
    index = 0
    current = []
    arr.sort()
    print(subset_sum_2(arr, index, result, current))

