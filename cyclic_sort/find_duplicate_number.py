# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
# The array has only one duplicate but it can be repeated multiple times. 
# Find that duplicate number without using any extra space. You are, however, 
# allowed to modify the input array.

def duplicate_number(arr):
    start = 0

    while start < len(arr):
        pointer_to_compare = arr[start] - 1

        if arr[start] != arr[pointer_to_compare]:
            arr[start] , arr[pointer_to_compare] = arr[pointer_to_compare], arr[start]
        else:
            start+=1
        
    # now array is sorted 
    #  we can put this loop inside the above loop 
    for i in range(len(arr)):
        if i+1 != arr[i]:
            return arr[i] 
        
    return -1

if __name__=="__main__":

    arr= [1,4,4,3,2]
    print(duplicate_number(arr))