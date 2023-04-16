# util for binary search recursive 
 
def binary_search(arr,target, left ,right):
    

    while(left <= right):
        mid = left + (right - left) //2

        if arr[mid] == target:
            return mid 

        elif arr[mid] > target:
            return binary_search(arr, target, left, mid-1)
        
        else:  
            return binary_search(arr, target, mid+1, right)
        

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    target = 4
    left = 0
    right = len(arr) - 1
    result = binary_search(arr, target, left, right)
    print(result)

        
