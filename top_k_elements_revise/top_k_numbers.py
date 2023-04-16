import heapq

def top_k_numbers(arr, k):
    minheap = []
    ## making minheap of the elements of k lenght
    for i in range(k):
        heapq.heappush(minheap, arr[i])
    
    # now compare the array elements which are greater than the minheap root(smallest element) and 
    # exchange those elements 

    for i in range(k, len(arr)):

        if arr[i] > minheap[0]:
            heapq.heappop(minheap)
            heapq.heappush(minheap, arr[i])
    
    return minheap


if __name__=="__main__":
    arr= [1,2,3,4,5,6]
    k=3

    print(top_k_numbers(arr,k))