#Given the root node of a binary tree, convert the binary tree into its mirror image.

from build_tree import *

def invert(root):
    if not root:
        return None

    if root.left:
        invert(root.left)
    
    if root.right:
        invert(root.right)

    root.left , root.right = root.right, root.left

    return root


if __name__=="__main__":

    #root = build_tree([1,2,3])
    root = build_tree([10,5,20,2,7])
    
    invert_root = invert(root)

    print_tree(invert_root)