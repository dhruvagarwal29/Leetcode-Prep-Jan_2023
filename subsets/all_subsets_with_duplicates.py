# given a set of numbers that might contain duplicates, find all of its distinct numbers

def find_subsets(nums):
    # sort the numbers to handle duplicates
    list.sort(nums)
    result = []
    result.append([])
    start_index , end_index = 0 , 0

    for i in range(len(nums)):
        start_index=0
        # if current and the previous elements are same, create new subsets only from the subsets 
        # added in previous step
        if i > 0 and nums[i] == nums[i-1]:
            start_index = end_index + 1
        
        end_index = len(result) - 1

        for j in range(start_index, end_index + 1):
            # create a new subset from the existing sunset and add the current element to it

            new_set = list(result[j])
            new_set.append(nums[i])
            result.append(new_set)
    
    return result

if __name__=="__main__":
    arr = [1,3,3]
    print(find_subsets(arr))