# print the subsequences whose sum is k 

# two pointers O(n)


def subsequences_k_sum(arr, target):
    n = len(arr)
    start, end = 0, 0
    cur_sum = 0
    result = []
    
    while end < n:
        cur_sum += arr[end]
        while cur_sum > target and start <= end:
            cur_sum -= arr[start]
            start += 1
        if cur_sum == target:
            result.append(arr[start:end+1])
            cur_sum -= arr[start]
            start += 1
        end += 1
    
    return result


if __name__=="__main__":
    arr = [1,2,1]
    target = 2
    
    print(subsequences_k_sum(arr, target))