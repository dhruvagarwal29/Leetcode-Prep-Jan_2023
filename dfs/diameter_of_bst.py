class Treenode:
    def __init__(self,value,left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def diameter_of_tree(root):
    diameter_result = 0
    if not root:
        return 0, diameter_result
    else:
        # compute the height of tree and diameter
        height_bst, diameter_result = diameter_of_tree_recursive(root,diameter_result)

        return height_bst, diameter_result

def diameter_of_tree_recursive(root,diameter_result):
    
    if not root:
        return 0, diameter_result
    # traverse both the side of the tree 
    # first calculate left and the right
    left_tree_height, diameter_result = diameter_of_tree_recursive(root.left,diameter_result)
    right_tree_height, diameter_result = diameter_of_tree_recursive(root.right,diameter_result)

    # diameter of the current node will be equal to height of the left subtree + 
    # height of right subtree
    
    max_height = left_tree_height + right_tree_height

    diameter_result = max(diameter_result , max_height)

    return max(left_tree_height, right_tree_height) + 1, diameter_result

if __name__=="__main__":
    root = Treenode(1)
    root.left = Treenode(2)
    root.right = Treenode(3)
    root.left.left = Treenode(4)
    root.right.left = Treenode(5)
    root.right.right = Treenode(6)

    print(diameter_of_tree(root))

