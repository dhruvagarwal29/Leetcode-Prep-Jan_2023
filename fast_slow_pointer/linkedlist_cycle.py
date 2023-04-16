# find the cycle in linkedlist
# here we are using 2 pointers which will used to check if there is cycle in list 
# also known as hare and tortoise algorithm

class Node:
    def __init__(self,value, next = None):
        self.value = value
        self.next = next 

def has_cycle(head):
    slow, fast = head, head 

    while fast is not None and fast.next is not None :
        fast = fast.next.next
        slow = slow.next 
    
        if slow ==fast:
            return True
    return False


if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3) 
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)   
    print(has_cycle(head))
    head.next.next.next.next.next.next= head.next
    print(has_cycle(head))