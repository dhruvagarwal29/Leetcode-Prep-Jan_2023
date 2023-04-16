# given sorted array, and two integers 'K' and "X", find the K closest numbes to "X" in array.
# return the numbers in sorted order. 

# this is going to use two things binary search to find the closest number and then heap

# since array is sorted first find the closest number to X through binary search 

# k closest numbers will be adjacent to the discovered closest number from binary search in both directinio

# now use heap, we will push the absolute difference from X from these numbers in the min heap and 
# get the top k numbers from min heap 

def k_closest_numbers( arr, k , target):
    # find the closest number using binary search 

    left = 0 
    right = len(arr) -1

    while left <= right:
        mid = left + (right - left) //2 

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1


'''NOT complete '''