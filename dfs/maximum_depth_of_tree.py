# find the maximum depth of binary tree

from build_tree import *
def maximum_depth(root):
    if not root:
        return 0

    # traverse left and right trees 

    left_depth = maximum_depth(root.left)
    right_depth = maximum_depth(root.right)

    return max(left_depth ,right_depth) + 1

if __name__=="__main__":
    root = build_tree([1,2,3,4,5])

    print(maximum_depth(root))
