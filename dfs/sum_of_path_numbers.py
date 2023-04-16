#Given a binary tree where each node can only have a digit (0-9) value, 
# each root-to-leaf path will represent a number. 
# Find the total sum of all the numbers represented by all paths.


class Treenode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def sum_path(root):
    sum = 0

    if not root:
        return 0
    else:
        return sum_of_paths(root, sum)

def sum_of_paths(root, sum):
    if root is None:
        return 0
    
    # to add new value to path sum we have to multiply the sum by `10` and then add the number to it
    sum = sum * 10 + root.value

    # if root.left and left.right is none then return the sum
    if root.left is None and root.right is None:
        return sum 

    # add the sum of both the sides of trees
    return sum_of_paths(root.left, sum) + sum_of_paths(root.right, sum)

    return sum
if __name__=="__main__":
    root = Treenode(1)
    root.left = Treenode(0)
    root.right = Treenode(1)
    root.left.left = Treenode(1)
    root.right.left = Treenode(6)
    root.right.right = Treenode(5)
    print(sum_path(root))



        

