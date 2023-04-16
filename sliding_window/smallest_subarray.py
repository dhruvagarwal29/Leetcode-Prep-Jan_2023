# Smallest Subarray with a given sum (easy)


def bruteforce_subarray(arr, target):
    sum = 0
    min_length = float('inf')
    start = 0
    for end in range(0, len(arr)):
        sum += arr[end]  # adding the elements
        while sum >= target:
            min_length = min(min_length, end - start + 1)
            sum = sum - arr[start]
            start+=1

    return min_length


    # # for i in range(0,(len(a))):
    # while i<len(a):
    #     sum += a[i]
    #     # print(sum)
    #     a1.append(a[i]) 
    #     # print(a1)

    #     if sum >= target and len(result)<len(a1):
    #         result = a1
    #         sum = sum - a1[0]    
    #         a1.pop(0)      
    #         i+=1
    #         print(result)
    #     else:
    #         i+=1   
              
    # return result
        
if __name__ == "__main__":
    # a = [1,3,2,6,-1,4,1,8,2]
    a = [2, 1, 5, 2, 3, 2,8]
    k=7
    result = bruteforce_subarray(a,k)
    print(result)
    # print(len(result))