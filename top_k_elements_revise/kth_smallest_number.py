# find the kth smallest number from the unsorted array
from heapq import *
def kth_smallest(arr,k):
    # use max heap here --put k elemrnts in the heap and check all the other elements, 
    # if array has smaller element than the top of maxheap exchange it
    # in the end heap has the smallest element of size k and wew can result the top element of the heap

    maxheap = []

    for i in range(k):
        heappush(maxheap, -arr[i])# - is used as we are making max heap and inbuilt we have min heap

    for i in range(k, len(arr)):

        if arr[i] < -maxheap[0]:
            heappop(maxheap)
            heappush(maxheap, -arr[i])
        
    return -maxheap[0]


if __name__=="__main__":
    #arr= [1,5,12, 2, 11,5]
    arr= [5,12,11,-1,12]
    k=3
    print(kth_smallest(arr,k))