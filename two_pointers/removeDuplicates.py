# Problem Statement #
# Given an array of sorted numbers, remove all duplicates
#  from it. You should not use any extra space; after removing the
#   duplicates in-place return the new length of the array.

# def remove_duplicates(arr):  # first approach 
#     left = 1
#     right = 1

#     while(right!= len(arr)):
#         if arr[left-1] != arr[right]:
#             arr[left] = arr[right]
#             left+=1
#         right+=1
    
#     return left

# another approach 
def remove_duplicates(arr):
    left = 0
    right = 1
    while(right < len(arr)):
        if arr[right] != arr[left]:
            left+=1
            arr[left] = arr[right]        
        right+=1    
    return left+1
if __name__ =="__main__":

    #arr = [2, 3, 3, 3, 6, 9, 9]
    arr = [2, 2, 2, 11]
    len = remove_duplicates(arr)

    print(len)