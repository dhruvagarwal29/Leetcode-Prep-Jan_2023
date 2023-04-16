# find all the duplicate numbers in the array 

def duplicate_numbers(arr):
    # first sort the array 
    start = 0
    while start < len(arr):
        pointer_to_compare = arr[start] -1

        if arr[start] != arr[pointer_to_compare]:
            arr[start], arr[pointer_to_compare] = arr[pointer_to_compare], arr[start]
        else:
            start+=1

    result = []
    # now check for the duplicates 
    for i in range(len(arr)):
        if i+1 != arr[i]:
            result.append(arr[i])
    return result

if __name__=="__main__":
    arr = [3,4,4,5,5]
    print(duplicate_numbers(arr))
