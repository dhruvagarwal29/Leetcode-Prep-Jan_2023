# find the diameter of bst 

# for this we have to find the height of the tree

class Treenode:
    def __init__(self, value, left= None, right= None):
        self.value = value
        self.right = right
        self.left = left
    
def diameter_of_tree(root):

    diameter = 0
    
    if not root:
        return 0
    
    def diameter_of_tree_recursive(root):
        # defining the nonlocal variable here to update the diameter 
        nonlocal diameter
        if not root:
            return 0
        
        left_height = diameter_of_tree_recursive(root.left)
        right_height = diameter_of_tree_recursive(root.right)

        diameter = max(diameter, left_height + right_height) # this line is for diameter of the subtree 
 
        return 1 + max(left_height , right_height) # this line is for height of subtree
    
    diameter_of_tree_recursive(root)
    return diameter

if __name__=="__main__":
    root = Treenode(1)
    root.left = Treenode(2)
    root.right = Treenode(3)
    root.left.left = Treenode(4)
    root.right.left = Treenode(5)
    root.right.right = Treenode(6)

    print(diameter_of_tree(root))


