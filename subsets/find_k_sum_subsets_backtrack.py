# find all the subsets using backtrack

def find_k_subsets(arr, target):

    result = []
    for i in range(len(arr)):
        if arr[i] < target:
            current_list : list = [arr[i]]
            remaining_list : list = arr[i+1:] 
            backtrack(current_list, remaining_list, target, result)
        elif arr[i] == target:
            result.append(arr[i])
        else:
            continue
    
    return result

def backtrack(current_list : list , remaining_list : list , target : int , result : list):
    # print(current_list)
    # print(remaining_list)
    if sum(current_list) == target:
        result.append(list(current_list))
        return
    if sum(current_list) > target:
        return 
    
    
    for j in range(len(remaining_list)):
        c : int  = remaining_list[j]
        current_list.append(c)
        backtrack(current_list, remaining_list[j+1:],target, result)
        current_list.pop()
    

if __name__=="__main__":
    arr= [1,3,5,21,19,7,2]
    target = 10
    #print(k_sum_subsets(arr,target))
    print(find_k_subsets(arr,target))

    



