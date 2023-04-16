# given n ropes, need to connect to make a big rope woth min cost
# the cost of connecting 2 ropes is equal to sum of their lengths
from heapq import *
def ropes(arr):
    # use min heap here and put the 2 min ropes together and place them in the minheap again
    minheap=[]
    for i in range(len(arr)):
        heappush(minheap, arr[i])

    temp = 0 
    result = 0

    while len(minheap)>1: # this is the breaking point in this as we have to give one rope only
        temp = heappop(minheap) + heappop(minheap)
        result += temp # this is saving the rope and making it in smallest cost
        heappush(minheap, temp)
    
    return result

if __name__=="__main__":
    arr= [1,3,11,5]
    print(ropes(arr))