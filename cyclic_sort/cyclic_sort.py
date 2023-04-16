# make the sort in  O(n) sorting algos

def cyclic_sort(arr):
    start = 0   # make the original pointer here 

    while start < len(arr):
        # this pointer is equal to the values in arr and we are decreasing 1 from it as 
        # arr starts from 1 not 0 

        pointer_to_compare = arr[start] - 1
        # so if these indexes are not equal then swap them and so at 
        #print(arr[start] , arr[pointer_to_compare])
        if arr[start] != arr[pointer_to_compare]:
            # swap 
            arr[start], arr[pointer_to_compare] = arr[pointer_to_compare], arr[start]
        else:
            # increase the start variable 
            start+=1 
        
    return arr

if __name__=="__main__":
    arr = [3,1,5,4,2]

    print(cyclic_sort(arr))