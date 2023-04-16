#  Design a class to calculate the median of a number stream. The class should have the
#  following two methods:

# insertNum(int num): stores the number in the class
# findMedian(): returns the median of all numbers inserted in the class
# If the count of numbers inserted in the class is even, the median will be the average
#  of the middle two numbers.

'''
 the median is the middle value in an ordered integer list.
'''

from heapq import * 
class median:
    # we are using 2 heaps in this question to make it in O(log n) complexity 
    # here first half of the strea mwill remain in min heap and other half will be in maxheap 
    # if len of both the heaps are same then  take the top element out and their average is mean 
    # otherwise if no of streams is odd tben we addd one more extra element in maxheap and that is
    # the median of the stream 
    min_heap = []
    max_heap = []

    def insertNum(self, num): 
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
    
        '''
        Now for ques both the heaps have same length or maxheap will have 1 more element than minheap

        # we are saving small numbers in max heap 
        and large numbers in min heap as we get the maximum of small numbers in max heap as first element
        '''

        if len(self.max_heap) < len(self.min_heap):
            temp = heappop(self.min_heap)
            heappush(self.max_heap, -temp)
        # if max heap is filled more than one element then pop from it and put the -num in minheap
        # as we have saved negative element in max heap    
        if len(self.max_heap) > len(self. min_heap) + 1:
            temp = heappop(self.max_heap)
            heappush(self.min_heap, -temp)
        

    def find_median(self):
        # if the lenght of minheap and maxheap is equal then take the average of top elements of both heap 
        print("minheap=",self.min_heap)
        print("maxheap=", self.max_heap)
        if len(self.min_heap) == len(self.max_heap):
            # take the average 
            _median = (-self.max_heap[0] + self.min_heap[0]) / 2.0 

            return _median
        # if length is not equal then we have one extra element in maxheap that is median so return that

        return -self.max_heap[0] 


if __name__=="__main__":
    # make object for the class

    median_class = median()
    median_class.insertNum(3)
    median_class.insertNum(1)
    median_class.insertNum(5)
    print(median_class.find_median())