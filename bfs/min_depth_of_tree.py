# FIND THE MIN DEPTH OF TREE

from collections import deque

class Treenode:
    def __init__(self,value) -> None:
        self.value=value
        self.left = None
        self.right = None
    
def min_depth(root):
    if not root:
        return 0

    queue = deque()
    queue.append(root)
    min_depth = 0
    while queue:
        
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.popleft()
            min_depth+=1
            if not current_node.left or not current_node.right:
                return min_depth

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right) 

if __name__=="__main__":
    root = Treenode(12)
    root.left = Treenode(7)
    root.right = Treenode(1)
    root.right.left = Treenode(10)
    root.right.right = Treenode(5)

    print(min_depth(root))