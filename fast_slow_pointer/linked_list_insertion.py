class Node:
    def __init__(self,value, next = None) -> None:
        self.value = value
        self.next= next
    
def prepare_linked_list(head, node_list):
    current = head
    for item in node_list:
        new_node = Node(item)
        current.next = new_node
        current = new_node   
    return head


def print_list(head):
    temp = head 
    while temp:
        print(temp.value)
        temp = temp.next

if __name__=="__main__":
    head = Node(1)
    head = prepare_linked_list(head ,[2,3,4,5,6])
    print_list(head)