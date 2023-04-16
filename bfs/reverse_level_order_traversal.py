# populate an array to represent levels of binary tree in reverse order 

from collections import deque
class Treenode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def reverse_traversal(root):
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)

    while queue:
        # find the lenght of the queue as level size 
        level_size = len(queue)
        current_level = []

        for i in range(level_size):
            current_node = queue.popleft()
    
            # put the value of current_node in the current_level
            current_level.append(current_node.val)

            # if current node has child add them in queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
        result.insert(0, current_level)
        # we can use append as well and then return result[::-1]

    return result


def main():
    root = Treenode(12)
    root.left = Treenode(7)
    root.right = Treenode(1)
    root.left.left = Treenode(9)
    root.right.left = Treenode(10)
    root.right.right = Treenode(5)
    print(reverse_traversal(root))

main()