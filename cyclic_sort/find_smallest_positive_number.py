#Find the Smallest Missing Positive Number (medium) #

#Here the trick is to skip the negative elements from the array 

def smallest_number(arr):
    # skip the negative number
    start = 0 
    while start < len(arr):
        pointer_to_compare = arr[start] -1 
        
        if arr[start]>0 and arr[start] != arr[pointer_to_compare]:
            arr[start], arr[pointer_to_compare] = arr[pointer_to_compare], arr[start]
        else:
            start+=1
        
    for i in range(len(arr)):
        if i+1 != arr[i]:
            return i+1 
    
    return -1


if __name__=="__main__":
    arr = [-3, 1, 5, 4, 2]

    print(smallest_number(arr))