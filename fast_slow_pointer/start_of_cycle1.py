# this is another way of find the start of cycle by using the lenght of cycle 
class Node:
    def __init__(self, value, next =None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow = head 
    fast = head
    cycle_leng = 0
    while fast and fast.next:
        slow= slow.next
        fast = fast.next.next 
        if fast == slow:
            cycle_leng = find_length_cycle(slow)
            break
    if fast != slow:
        return "No Cycle"
    return start_of_cycle(head, cycle_leng)

def find_length_cycle(slow):  # this loop is used to find the length of cycle length
    current = slow 
    cycle_len = 0
    while True:
        current = current.next 
        cycle_len +=1
        if current == slow:
            break
    return cycle_len

def start_of_cycle(head, cycle_leng):
    pointer1= head 
    pointer2 = head
    # this loop will make the pointer2 ahead of pointer1 by the length of cycle 
    while cycle_leng > 0:
        pointer2 = pointer2.next
        cycle_leng -=1

    # now pointer1 is at head and pointer2 is at head+cycle_length

    # now incerment both the pointers until they meet each other at the start of cycle

    while pointer1 != pointer2:  # increment the pointers till they are equal 
        pointer1 = pointer1.next
        pointer2 = pointer2.next 
    
    # once they are equal return the value of pointer1 or pointer2 value
    return pointer1.value


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