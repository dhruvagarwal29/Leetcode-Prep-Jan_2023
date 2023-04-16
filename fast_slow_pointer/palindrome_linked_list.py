class Node:
    def __init__(self, value, next=None) -> None:
        self.value= value
        self. next = next

def palindrome_linkedlist(head):
    
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
    
    # now reverse the second half of the linked list 
    #print_list(slow)
    reverse_list_pointer = reverse_linked_list(slow)
    
    # store the second half of the linked lis
    
    slow = head 
    while slow and reverse_list_pointer:
        if slow.value != reverse_list_pointer.value:
            return False
        else:
            slow = slow.next
            reverse_list_pointer = reverse_list_pointer.next
    
    return True


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
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6) 
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    # head.next.next.next.next.next = Node(6)   
    # head.next.next.next.next.next.next = Node(7)   
    print(palindrome_linkedlist(head))
    