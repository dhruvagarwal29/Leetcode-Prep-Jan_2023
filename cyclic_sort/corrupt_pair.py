# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
# The array originally contained all the numbers from 1 to ‘n’, but due to a data error, 
# one of the numbers got duplicated which also resulted in one number going missing. 
# Find both these numbers.

def corrupt_pair(arr):
    # sort the array 
    start = 0 
    while start < len(arr):
        pointer_to_compare = arr[start] - 1
        if arr[start] != arr[pointer_to_compare]:
            arr[start], arr[pointer_to_compare] = arr[pointer_to_compare], arr[start]
        else:
            start +=1
    # now find the corrupt pair
    for i in range(len(arr)):
        if i+1 != arr[i]:
            return [arr[i], i+1]
    

if __name__=="__main__":
    arr = [ 3,1,2,5,2]
    [a,b]=(corrupt_pair(arr))
    print("Dulicate->", a, "Missing->",b)