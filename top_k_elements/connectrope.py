# Connect Ropes
import heapq
def topk(a):
    minheap = []
    cost = 0
    temp = 0
    for i in range(len(a)):
        heapq.heappush(minheap, a[i])
    
    
    while len(minheap) > 1:
        temp = heapq.heappop(minheap) + heapq.heappop(minheap)
        cost = cost + temp
        heapq.heappush(minheap, temp)
    return cost


if __name__ == "__main__":

    a = [1, 3, 11, 5,2]
    
    result = topk(a)

    print(result)
