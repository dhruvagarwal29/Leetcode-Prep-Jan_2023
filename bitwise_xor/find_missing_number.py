# we have array of n-1 numbers range from 1 to n find the missing number

def missing_number(arr):
    # arr is of n-1 size , we are going to use the sum of the numbers till n and then subtract the array, so the 
    # remaining number will be the missing number
    final_size = len(arr) + 1

    sum = 0

    for i in range(1, final_size+1):
        sum += i
    
    #print(sum)
    for i in range(len(arr)):
        sum -= arr[i]
    return sum 

if __name__=="__main__":
    arr= [1,2,4,5,6]
    print(missing_number(arr))

''' But here we have one problem with this solution and that is we can get interger overflow when n is large'''
# to solve this issue we are going to use the XOR bitwise pattern 
