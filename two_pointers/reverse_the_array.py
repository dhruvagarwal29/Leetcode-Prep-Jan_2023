# reverse the array 

def reverse(arr):
    left = 0
    right = len(arr)-1
    temp = ''
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp 

        left+=1 
        right -=1
    
    return arr


if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    str = "abc"
    result = reverse(str)
    print(result)    