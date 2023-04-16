# brute force 
# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.


# def bruteforce_subarray(a, k):
#     result = []

#     for i in range(0,(len(a))-k+1):
#         sum = 0
#         # print(i)
#         for j in range(i , i+k):
#             sum += a[j]
#         result.append(sum/k)  
#     return result

def subarray(a, k):   # O(n) complexity
    result = []
    sum = 0
    for i in range(0,len(a)):
        if i < k:
            sum += a[i]
        else:
            result.append(sum/k)
            sum = sum - a[i-k] + a[i]   
    result.append(sum/k) 
    return result


if __name__ == "__main__":
    a = [1,3,2,6,-1,4,1,8,2]
    k=5
    result = subarray(a,k)

    print(result)

