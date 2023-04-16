#Serialize a given binary tree to a file and deserialize it back to a tree.
#  Make sure that the original and the deserialized trees are identical.

# Serialize: Write the tree to a file.

# Deserialize: Read from a file and reconstruct the tree in memory.

# Serialize the tree into a list of integers, and then, deserialize it back from the list to a tree. 
# For simplicity’s sake, there’s no need to write the list to the files.

'''
 check this again as it is giving errors in serializing 
'''
from build_tree import *

# defining the marker for none values to add in the tree
MARKER = "M"
counter = 1

# fucntion to serialize the streams 
def serialize(root):
    list_bst = []
    serialize_recursive(root, list_bst)
    return list_bst
def serialize_recursive(root, list_bst):
    global counter
    
    if root is None:
        # list_bst.append(MARKER + str(counter))
        # counter += 1
        return
    # print("serrialise")
    # print_tree( root)
    # adding node to list
    list_bst.append(root.value)

    # pre order traversal for the serialization 
    serialize_recursive(root.left, list_bst)
    
    serialize_recursive(root.right, list_bst)


# function to deserialize the streams

def deserialize(list_bst):
    root = build_tree(list_bst)
    return root
    
if __name__=="__main__":

    root = build_tree([1,2,3,4,5])
    print_tree(root)
    stream = serialize(root)
    print(stream)
    print_tree(deserialize(stream))