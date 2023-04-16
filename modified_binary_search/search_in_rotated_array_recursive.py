# modified binary search question 

# you have given a rotated array find the index of the given target

# recursive way 
def rotated_binary_array(arr, target, left, right):


    while left <= right:
        mid= left + (right - left )//2

        if target == arr[mid]:
            return mid

        # now check if left to mid array is sorted 

        if arr[left] <= arr[mid]:
            # now check if target is in this section of the array 
            if arr[left] <= target and target < arr[mid]:
                return rotated_binary_array(arr, target,left, mid-1)
                
            else: # if target is on the other half of the array
                return rotated_binary_array(arr, target, mid + 1, right) 
                
    
            
        else: # here it means that the mid to right array is sorted 
            if target > arr[mid] and target <= arr[right]: 
                # check if target is present in mid to right where array is sorted 
                return rotated_binary_array(arr, target, mid + 1, right)
            else:
                # here it means that target is not in the sorted section of the arrray 
                return rotated_binary_array(arr, target,left, mid-1) 

   

if __name__=="__main__":
    arr = [11, 15, 200, 432, 765, 1000]
    target =15
    left = 0
    right = len(arr) -1 
    print(rotated_binary_array(arr, target,left,right))