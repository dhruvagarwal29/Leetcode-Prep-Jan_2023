# reverse the array by recursion
# two pointers 
def rever(arr, left, right):

    if left >= right:
        return arr
    
    arr[left], arr[right] = arr[right], arr[left]
    
    rever(arr, left+1, right-1)

    return arr


# we can use as sigle pointer also
# first pointer will be i , starting from 0 another pointer will be n-i-1 where n is len(arr)

def reverse_single_pointer(arr, i, n):
    if i >= n/2:
        return 
    
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    reverse_single_pointer(arr, i+1, n)

    return arr



def main():
    arr= [1,2,3,4,5]
    left = 0
    right = len(arr) -1 
    n= len(arr)
    # print(rever(arr, left, right))
    print(reverse_single_pointer(arr, left, n))

main()
    
    