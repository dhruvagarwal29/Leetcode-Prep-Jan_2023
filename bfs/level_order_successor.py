# find the node value that appear right after the given node 

from collections import deque
class Treenode:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

def level_order_successor(root, key_node):

    if not root:
        return -1
    
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.popleft()

            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)
            

            if current_node.value == key_node:
                return queue[0].value
            else: return None
    

def main():
    root = Treenode(12)
    root.left = Treenode(7)
    root.right = Treenode(1)
    root.left.left = Treenode(9)
    root.right.left = Treenode(10)
    root.right.right = Treenode(5)
    print(level_order_successor(root, 12))
    print(level_order_successor(root, 11))

main()