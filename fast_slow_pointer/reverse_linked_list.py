class Node:
    def __init__(self, value, next=None) -> None:
        self.value= value
        self. next = next

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
    head.next.next.next.next.next.next = Node(7)   
    print_list((reverse_linked_list(head)))
    