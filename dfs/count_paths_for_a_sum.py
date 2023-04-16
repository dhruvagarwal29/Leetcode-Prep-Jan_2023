# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all 
# the node values of each path equals ‘S’. Please note that the paths can start or end at any 
# node but all paths must follow direction from parent to child (top to bottom).


class Treenode:
    def __init__(self,value, left=None, right= None):
        self.value = value
        self.left = left
        self.right = right

def count_path_sum(root, target_sum):
    current_path = []
    if not root:
        return 0
    else:
        return current_path_sum_recursive(root, current_path, target_sum)

def current_path_sum_recursive(root, current_path, target_sum):
    # if not root return 0
    if not root:
        return 0
    
    # current_path is a list in which we are pushing the value
    current_path.append(root.value)

    # now check if current path has values which are equal to targert value by traversing current_path in
    # reverse 

    path_sum = 0 # to count the value from current path 
    path_count = 0 # to store the correct paths 

    for i in range(len(current_path)-1 ,-1 ,-1):# traverse the list (currentpath) in reverse
        path_sum += current_path[i] # add the current path recent value in path sum

        if path_sum == target_sum: # if path sum is equal to target sum then increase the path count
            path_count += 1 


    # add the path counts from both the side of the tree left and right
    path_count += current_path_sum_recursive(root.left, current_path, target_sum)
    path_count += current_path_sum_recursive(root.right, current_path, target_sum)

    # remove the current path to use for other path 
    current_path.pop()

    return path_count

if __name__=="__main__":
    root = Treenode(1)
    root.left = Treenode(7)
    root.right = Treenode(9)
    root.left.left = Treenode(6)
    root.left.right = Treenode(5)
    root.right.left = Treenode(2)
    root.right.right = Treenode(3)
    target =12
    print(count_path_sum(root, target))