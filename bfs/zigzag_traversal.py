from collections import deque
class Treenode:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
def zigzag_traversal(root):
    result = []
    if not root:
        return result
    
    queue = deque()
    queue.append(root)
    switch_the_order = True
    while queue:
        
        level_size = len(queue)
        current_level = []

        for i in range(level_size):
            currrent_node = queue.popleft()

            if not switch_the_order: # zigzag traversal
                current_level.insert(0,currrent_node.value)
            else:
                current_level.append(currrent_node.value)
            
            if currrent_node.left:
                queue.append(currrent_node.left)
            if currrent_node.right:
                queue.append(currrent_node.right)
            
        result.append(current_level)
        switch_the_order = not switch_the_order
    
    return result

if __name__=="__main__":
    root = Treenode(12)
    root.left = Treenode(7)
    root.right = Treenode(1)
    root.left.left = Treenode(9)
    root.right.left = Treenode(10)
    root.right.right = Treenode(5)
    root.right.left.left = Treenode(20)
    root.right.left.right = Treenode(17)

    print(zigzag_traversal(root))
