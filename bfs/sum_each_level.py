# find the sum at each level 

from collections import deque

class Treenode:
    def __init__(self, value) -> None:
        self.value = value
        self.right= None
        self.left = None

def level_sum(root):
    result = []
    if not root:
        return result
    
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        sum = 0

        for i in range(level_size):
            current_node = queue.popleft()
            sum+= current_node.value

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)
            
        result.append(sum)
    
    return result
    
if __name__=="__main__":
    root = Treenode(12)
    root.left = Treenode(7)
    root.right = Treenode(1)
    root.left.left = Treenode(9)
    root.right.left = Treenode(10)
    root.right.right = Treenode(5)

    print(level_sum(root))