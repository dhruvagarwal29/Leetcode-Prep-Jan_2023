import heapq

def topk(a,k):
    result = []

    for i in range(0,k):
        heapq.heappush(result, a[i])
    

    for i in range(k, len(a)):
        if a[i] > result[0]:
            heapq.heappop(result)
            heapq.heappush(result, a[i])
    
    return result

if __name__ == "__main__":
    #a = [1,3,2,6,-1,4,1,8,2]

    a = [3,1,5,12,2,11]
    k = 3
    #k=5
    result = topk(a,k)

    print(result)
