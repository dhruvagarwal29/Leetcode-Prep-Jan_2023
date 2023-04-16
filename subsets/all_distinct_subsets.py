# Given a set with distict elements, find all of its distinct subsets

def all_subsets(arr):
    result = [[]]
    # result.append([])
    for num in arr:
        current_size = len(result)
        for i in range(current_size):
            # make a copy of result list 
            copy_list = list(result[i])
            copy_list.append(num)
            result.append(copy_list)

    return result


if __name__=="__main__":
    arr= [1,3]
    print(all_subsets(arr))
