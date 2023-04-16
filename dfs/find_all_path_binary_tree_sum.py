#Given a binary tree and a number ‘S’, 
# find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

class Treenode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def find_all_paths(root, sum):
    all_paths = []
    find_all_path_recursive(root, sum, [], all_paths)
    return all_paths

def find_all_path_recursive(root, sum, current_path, all_paths):
    if root is None:
        return

    # add the current root to the current path
    current_path.append(root.value)

    # when to add the path in all_paths 
    if root.value == sum and root.left is None and root.right is None:
        all_paths.append(current_path[:]) 
    else:
        # now make recursive calls
        find_all_path_recursive(root.left, sum - root.value, current_path, all_paths)
        find_all_path_recursive(root.right, sum - root.value, current_path, all_paths)
    
    current_path.pop() # removing the current path after one true so other path can be saved 
     

if __name__=="__main__":
    root = Treenode(12)
    root.left = Treenode(7)
    root.right = Treenode(1)
    root.left.left = Treenode(4)
    root.right.left = Treenode(10)
    root.right.right = Treenode(5)

    print(find_all_paths(root, 23))
    

        