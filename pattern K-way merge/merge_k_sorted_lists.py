# Problem Statement #
# Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

import heapq

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge_lists(lists):
    minHeap = []

    for root in lists:
        if root is not None:
            heapq.heappush(minHeap, root)


if __name__ == "__main__":
    
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2,l3])