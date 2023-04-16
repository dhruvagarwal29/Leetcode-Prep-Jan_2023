class Node:
    def __init__(self, value, next=None) -> None:
        self.value= value
        self. next = next

def middle_of_linked_list(head):
    slow = head
    fast = head 

    while fast and fast.next:
        fast = fast.next.next 
        slow = slow.next
    
    return slow.value


if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3) 
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    # head.next.next.next.next.next = Node(6)   
    # head.next.next.next.next.next.next = Node(7)   
    print(middle_of_linked_list(head))
    