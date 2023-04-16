# given the head of singly linked list, write a method to modify linked list such that nodes from 
# the second half of the linked list are inserted alternately to the nodes from the first in reverse 
# order.  example 1-2-3-4-5-6 output;- 1-6-2-5-3-4

class Node:
    def __init__(self, value, next=None) -> None:
        self.value= value
        self. next = next

def rearrange_linked_list(head):
    
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
    
    # now reverse the second half of the linked list 
    head_second_half = reverse_linked_list(slow)
    
    # store the second half of the linked list
    
    head_first_half = head # first half of linked list 
    # print_list(head_first_half)
    # print('\n')
    # print_list(head_second_half)
    while head_first_half and head_second_half:
        
        temp = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = temp 

        temp = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half= temp 

    if head_first_half is not None:
        head_first_half.next = None
    
    return head


def reverse_linked_list(head):
    prev = None 
    while head is not None:
        next = head.next 
        head.next = prev 
        prev = head 
        head = next  
    return prev

def print_list(head):
    current = head 
    while current:
        print(current.value)
        current = current.next

if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3) 
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)   
    # head.next.next.next.next.next.next = Node(7)   
    print_list(rearrange_linked_list(head))
    