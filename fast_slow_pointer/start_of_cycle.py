# find the cycle in linkedlist
# here we are using 2 pointers which will used to check if there is cycle in list 
# also known as hare and tortoise algorithm

class Node:
    def __init__(self,value, next = None):
        self.value = value
        self.next = next 
    
# this is used to print the list
# def print_list(head):   
#     temp = head
#     while temp is not None:
#         print(temp.value, end= " ")
#         temp = temp.next
#     # print('\n')
    
def has_cycle(head):
    slow, fast = head, head 
    cycle_exist = False
    #print_list(head)
    while fast is not None and fast.next is not None :
        fast = fast.next.next
        slow = slow.next 
    
        if slow == fast:
            cycle_exist = True
            break
    # if slow != fast:   # if list has no cycle in it
    #     print("No cycle found")

    if cycle_exist == False:
        print("No cycle found")
        
    if cycle_exist:
        slow = head
        while (slow != fast):
            slow = slow.next
            fast = fast.next
        print(slow.value)


# def cycle_length(slow):
#     current = slow 
#     cycle_len = 0
#     while True:
#         current = current.next
#         cycle_len +=1 
#         if current == slow:
#             break 
#     return cycle_len


if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3) 
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)   
    has_cycle(head)
    # head.next.next.next.next.next.next= head.next
    # has_cycle(head)