#Given the root of a binary tree, flatten the tree into a linked list using the same Tree class.
#  The left child of the linked list is always NULL, and the right child points to the next node in 
# the list. The nodes in the linked list should be in the same order as the preorder 
# traversal of the given binary tree.

class Treenode:
    def __init__(self,value, left=None, right= None):
        self.value = value
        self.left = left
        self.right = right

def flatten_tree(root):
    linked_list = [] # to save the tree
    if not root:
        return 0
    else:
        return flatten_tree_recursive(root, linked_list)


def flatten_tree_recursive(root, linked_list):
    if not root:
        return 0

    # append the current value in the linked list
    linked_list.append(root.value)

    flatten_tree_recursive(root.left, linked_list)
    flatten_tree_recursive(root.right, linked_list)

    return linked_list

if __name__=="__main__":
    root = Treenode(1)
    root.left = Treenode(7)
    root.right = Treenode(9)
    root.left.left = Treenode(6)
    root.left.right = Treenode(5)
    root.right.left = Treenode(2)
    root.right.right = Treenode(3)
    
    print(flatten_tree(root))