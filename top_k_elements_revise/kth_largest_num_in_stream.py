# design a class to effeciently find the kth largest element in a stream of numbers 
'''
The class should have:
1) constructor of class should accept an interger array containing nos of string and integer "K"
2) class should expose a function add(int num) which will store the given number and return kth largest
'''
from heapq import *
class KthLargestNumberInStream:
    minHeap = []
    def __init__(self, nums, k):
        self.k=k

        # from the stream of numbers add these in the minHeap by calling add function
        for num in nums:
            self.add(num)

        
    def add(self, num):
        heappush(self.minHeap, num)

        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
    
        return self.minHeap[0]
    

if __name__=="__main__":
    # making object of the class KthLargestNumberInStream 
    nums = [3,1,5,12,2,11]
    k = 4
    kthLargestNumber = KthLargestNumberInStream(nums, k)

    print(kthLargestNumber.add(6))
    print(kthLargestNumber.add(13))
    print(kthLargestNumber.add(4))
        
