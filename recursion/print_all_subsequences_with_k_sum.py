# print the subsequences whose sum is k 

# recursion


def subsequences_k_sum(arr, current_index, target, result, current):

    if current_index == len(arr): 
        if sum(current) == target:
            result.append(list(current))
            return
        else:
            return

    current.append(arr[current_index]) 
    subsequences_k_sum(arr, current_index+1, target, result, current)# take the value 
    current.pop()
    subsequences_k_sum(arr, current_index+1, target, result, current)# not take the value         
    return result


if __name__=="__main__":
    arr = [1,2,1]
    target = 2
    
    current_index = 0
    print(subsequences_k_sum(arr, current_index, target, [], []))