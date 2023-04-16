# wap to print all the subsequences of the given array 

def subsequences(arr,current_index, result,current):
    # take and not take values of the arr
    
    if current_index == len(arr):
        result.append(list(current))
        '''
        list(current) creates a new list that contains the same 
        elements as the current list at that moment. This is
        necessary because otherwise, if the current list were directly 
        appended to the result list, any subsequent modifications to 
        current would also modify the previously appended subsequence in result.
        By creating a new list with the same elements, we ensure that
        each subsequence in result is unique and not affected by any 
        modifications made to current after its creation.
        '''
        return

    current.append(arr[current_index])
    subsequences(arr, current_index+1, result, current)
    current.pop()
    subsequences(arr, current_index +1, result,current)
    
    return result
    

if __name__=="__main__":
    arr = [1,2,3]
    result = []
    current_index = 0 
    res = []
    print(subsequences(arr,current_index, result, res))


# time complexity = O(2^n)
# space complexity = O(n)