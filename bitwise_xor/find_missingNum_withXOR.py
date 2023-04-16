# find the missing number using XOR pattern 
''' 0 xor any other number gives the same number  '''

def missing_number(arr):
    # length of the arr is n-1 as it has one element missing so final size will be length(arr) + 1
    final_size = len(arr) + 1

    # x1 represents xor of all values from 1 to n
    x1= 1
    for i in range(2,final_size+1):
        x1= x1 ^ i
        
    # x2 will get the xor values of array 
    x2 = arr[0]
    for i in range(1, len(arr)):
        x2 = x2 ^ arr[i]
        #print(x2)
 
    # missing number will be the xor of x1 and x2
    return x1 ^ x2


if __name__=="__main__":
    arr= [1,2,4,5]
    print(missing_number(arr))