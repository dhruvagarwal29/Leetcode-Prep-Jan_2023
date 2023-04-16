class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

def build_tree(node_list):
    left_child_index = 0
    right_child_index = 0

    # assigning root element from node_list
    root = Node(node_list[0])

    # using queue
    queue = []
    queue.append(root)

    i=0 
    while len(queue) > 0:
        current = queue.pop(0)
        left_child_index = (2 * i) + 1
        right_child_index = (2 * i) + 2

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
