class Treenode:
    def __init__(self,value, left= None, right= None) -> None:
        self.value = value
        self.left = left
        self.right = right

def has_path(root, sum):
    
    if root is None:
        return False
    
    # when to say true 
    # if current node is leaf node and its value is equal to sum, we've found the path 
    if root.value==sum and root.left is None and root.right is None:
        return True

    # recursively call to traverse the left and right sub tree
    # return true if any of the subtree returns true

    return has_path(root.left, sum - root.value) or has_path(root.right, sum - root.value)

if __name__=="__main__":
    root = Treenode(12)
    root.left = Treenode(7)
    root.right = Treenode(1)
    root.left.left = Treenode(9)
    root.right.left = Treenode(10)
    root.right.right = Treenode(5)

    print(has_path(root, 23))
    print(has_path(root, 16))



