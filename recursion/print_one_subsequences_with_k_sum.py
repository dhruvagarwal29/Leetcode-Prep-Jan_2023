# print only one the subsequences whose sum is k 

# recursion


def subsequences_k_sum(arr, current_index, target, result, current):

    if current_index == len(arr): 
        # condition satisfied
        if sum(current) == target:
            result.append(list(current))
            print(result)
            return True
        else: # condition not satisfied

            return False

    current.append(arr[current_index]) 
    if (subsequences_k_sum(arr, current_index+1, target, result, current)):# take the value 
        return True
    
    current.pop()
    if (subsequences_k_sum(arr, current_index+1, target, result, current)):# not take the value        
        return True
     
   


if __name__=="__main__":
    arr = [1,2,1]
    target = 2
    
    current_index = 0
    print(subsequences_k_sum(arr, current_index, target, [], []))