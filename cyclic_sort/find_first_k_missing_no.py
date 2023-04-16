# Find the First K Missing Positive Numbers (hard) #

#Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ 
# missing positive numbers in the array.

def k_missing_number(arr,k):
    
    # sort the array
    start = 0
    while start < len(arr):
        point_to_compare = arr[start] - 1
        if arr[start] > 0 and arr[start] <= len(arr) and arr[start] != arr[point_to_compare]:
            arr[start], arr[point_to_compare] = arr[point_to_compare], arr[start]
        else:
            start += 1
    print(arr)
    missing_numbers = []
    extra_numbers = set()
    # now we need to make a set that contains extra numbers so we can add the next number from it 
    # the next smallest missing 
    for i in range(len(arr)):
        if i+1 != arr[i]:
            missing_numbers.append(i+1)
            extra_numbers.append(arr[i])

    
if __name__=="__main__":
    # arr = [3,-1,4,5,5] 
    # k=3

    arr= [-2, -3, 4]
    k=2

    print(k_missing_number(arr,k))