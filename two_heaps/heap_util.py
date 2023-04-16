# Developing heap util for two heaps so I can use them again 
import heapq
from heapq import *

class MedianOfAStream:
    min_heap = []
    max_heap = []
    def insert_num(self,num):
        # inserting the numbers accordingly 
        '''
        we are making maxheap = minheap + 1 size 

        so if maxheap is empty or root element of maxheap is bigger than num then push the num into maxheap
        '''
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # here it is used to balance the heaps
        self.balance_heaps()

    
    def balance_heaps(self):

        # this function is to balancing the heaps
        
        if len(self.min_heap) > len(self.max_heap):
            # pop the element from min heap and push it into max heap
            heappush(self.max_heap, -(heappop(self.min_heap)))
        elif len(self.max_heap) > len(self.min_heap) + 1:
            # if len of maxheap > len minheap + 1 then pop it from max and push it into minheap
            heappush(self.min_heap, -(heappop(self.max_heap)))
        
    # to calculate median of 2 heaps
    def median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0] )/ 2.0
        else:
            return -self.max_heap[0]

    def remove_number(self, heap, element_to_remove):
        # find the index of the elememt_to_remove 

        index = heap.index(element_to_remove)
        # to maintain heap , put this element in the end of heap and then remove it

        heap[index] = heap[-1] # last element is the element to be deleted

        heap.pop() # element is removed from the heap 

        # now we have to heapify the heaps to readjust the elements but it will take O(N) time which is expensive
        # instead we will adjust only one element which will be O(log N)

        if index < len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)

