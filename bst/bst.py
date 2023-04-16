from collections import deque
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def bfs(root):
    queue = []
    result = []
    if root is None:
        return
    queue.append(root)
    queue.append(None)
    level = 0
    while queue:
        
        current_node = queue.pop(0)
        temp = []
        
        if current_node is None:
            level +=1
            if queue is not None: 
                queue.append(None)
        else:
            if current_node.left is not None:
                queue.append(current_node.left)
                temp.append(current_node.left.data)

            if current_node.right is not None:
                queue.append(current_node.right)  
                temp.append(current_node.right.data) 

    result.append(queue)

# def print(root): 
    
#     if root is None:
#         return

#     queue = []
#     result = []
#     rootlevel = []
#     l1 = [] 
#     l2 = []
#     queue.append(root)
#     result.append(root)

#     while(queue):
 
#         node = queue.pop(0)
 
#         if node.left is not None:
#             queue.append(node.left)
        
#         if node.right is not None:
#             queue.append(node.right)
        
#         # result.append(queue)
#         # print(result)

def level_order_traversal(root):
    result = []
    queue = []
    queue.append(root)
    queue.append(None)

    temp_list = []

    while len(queue) > 0:
        current = queue.pop(0)
        
        if len(queue) == 0:
            break

        if not current:
            current = queue.pop(0)
            queue.append(None)
            result.append(temp_list)
            temp_list = []

        temp_list.append(current.value)

        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)

    result.append(temp_list)

    return result


                
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
bfs(root)