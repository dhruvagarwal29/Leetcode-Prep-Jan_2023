# populate an array to represent levels of binary tree
from build_tree import *
from collections import deque 

class Treenode:
    def __init__(self,value) -> None:
        self.value = value 
        self.left = None
        self.right = None


def Traverse(root):
    result = []

    if not root:
        return result

    # maintain queue
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for i in range(level_size):
            current_node = queue.popleft()
            # add the element to the current level 
            current_level.append(current_node.value)
            # insert the children of current node in the queue
            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)
    
        result.append(current_level)
    
    return result

def main():
    root = Treenode(12)
    root.left = Treenode(7)
    root.right = Treenode(1)
    root.left.left = Treenode(9)
    root.right.left = Treenode(10)
    root.right.right = Treenode(5)

    # root = build_tree([12,7,1,9,10,5])

    print(Traverse(root))



main()