# Problem Statement #
# Design a class to efficiently find the Kth largest element in a stream of numbers.

# The class should have the following two things:

# The constructor of the class should accept an integer array 
# containing initial numbers from the stream and an integer ‘K’.
# The class should expose a function add(int num) 
# which will store the given number and return the Kth largest number.


# question is asking to print the kth largest number 

import heapq
class Kth_largest_element:
    minHeap = []
    def __init__(self,nums,k):
        self.k = k

        for n in nums:
            self.add(n)


    def add(self, num):
        heapq.heappush(self.minHeap, num)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]

if __name__ == "__main__":

    array =[3, 1, 5, 12, 2, 11]
    k = 4 

    result = Kth_largest_element(array, k)

    print(result.add(6))
    print(result.add(13))
    print(result.add(4))
    
