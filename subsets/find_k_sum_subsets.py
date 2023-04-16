#Given a set of n positive integers, find all the possible subsets of integers that sum up to a number k.
# brute force 
def k_sum_subsets(nums,target):

    result = []
    result.append([])
    for num in nums:
        current_size = len(result)

        for j in range(current_size):
            new_list = list(result[j])
            new_list.append(num)
            result.append(new_list)
    
    final_result = []
    for li in result:
        if sum(li) == target:
            final_result.append(li)
    return final_result


# more optmized 
def k_sum_subsets_optimized(nums,target):
    result = []
    result.append([nums[0]])
    for i in range(1,len(nums)):
        current_size = len(result)
        num = arr[i]
        if num <= target:
            result.append([num])
        

        for j in range(current_size):
            # getting the first number from list 
            new_list = list(result[j])
            if num + sum(new_list) <= target:
                new_list.append(num)
                result.append(new_list)
    
    final_result = []
    for li in result:
        if sum(li) == target:
            final_result.append(li)
    return final_result






if __name__=="__main__":
    arr= [1,3,5,21,19,7,2]
    target = 10
    #print(k_sum_subsets(arr,target))
    print(k_sum_subsets_optimized(arr,target))
