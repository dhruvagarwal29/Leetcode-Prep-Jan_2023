# find all the missing numbers from the array 
 # array is starting from 1

def all_missing_numbers(arr):
    #sort the arry using cyclic sort 
    start = 0

    while start < len(arr):
        pointer_to_compare = arr[start] - 1

        if arr[start] != arr[pointer_to_compare]:
            #swap 
            arr[start], arr[pointer_to_compare] = arr[pointer_to_compare], arr[start]
        else:
            start +=1 
    print(arr)
    # now the arr is sorted, check for missing values 
    result = []
    for i in range(len(arr)):
        
        if i+1 != arr[i]:
            result.append(i+1)

    return result 

if __name__=="__main__":
    # arr = [2,3,1,8,2,3,5,1]
    arr = [2,3,2,1]
    print(all_missing_numbers(arr))