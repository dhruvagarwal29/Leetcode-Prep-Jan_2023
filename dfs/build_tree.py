class Node:
    def __init__(self,value, left=None, right=None):
        self.value= value
        self.left = left
        self.right = right

    # def __repr__(self) -> str:
    #     return str(self.value)
        
    
def build_tree(node_list):
    left_child_index = 0
    right_child_index = 0

    root = Node(node_list[0]) # assign the root as 1st element of list

    # inintializing the queue
    queue = []
    queue.append(root)

    i=0

    while len(queue) > 0:
        current = queue.pop(0)
        left_child_index = (2*i) + 1
        right_child_index = (2*i) + 2

        if right_child_index < len(node_list):

            if node_list[left_child_index] or node_list[left_child_index] == 0:
                current.left = Node(node_list[left_child_index])
                queue.append(current.left)
            
            if node_list[right_child_index] or node_list[right_child_index] == 0:
                current.right = Node(node_list[right_child_index])
                queue.append(current.right)
            
        i+=1 
    
    return root


def print_tree(root):
    current = root

    queue = []
    queue.append(root)

    while len(queue) > 0:
        current = queue.pop(0)

        # print("Node: ", current.value)
        print(current.value)

        if current.left:
            #print("Node-left: ", current.left.value)
            queue.append(current.left)
        if current.right:
            #print("Node-right: ", current.right.value)
            queue.append(current.right)

if __name__ == "__main__":
    
    l = [1,2,3,None,None,4,5]
    root = build_tree(l)
    print_tree(root)

