#Given a binary tree and a number sequence, find if the sequence is present as
#  a root-to-leaf path in the given tree.


class Treenode:
    def __init__(self,value,left= None,right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

def find_sequence(root, sequence):
    if not root:
        return len(sequence) == 0
    else:
        return find_sequence_recusive(root, sequence,0)

def find_sequence_recusive(root, sequence,sequence_index):

    if root is None:
        return False

    seq_len = len(sequence)
     
    # if length of sequence_index greater than or equal to sequence length that means we have traversed 
    # or cross the whole sequence lenght in the tree but havent found the sequence so False  
    if sequence_index >= seq_len or root.value != sequence[sequence_index]:
        return False

    # if root.left and right is none anddd seq index is equal to sequence length -1 then it is true
    if root.left is None and root.right is None and sequence_index == seq_len  -1:
        return True

    return find_sequence_recusive(root.left, sequence, sequence_index + 1) or \
            find_sequence_recusive(root.right, sequence, sequence_index + 1)



if __name__=="__main__":
    root = Treenode(1)
    root.left = Treenode(0)
    root.right = Treenode(1)
    root.left.left = Treenode(1)
    root.right.left = Treenode(6)
    root.right.right = Treenode(5)
    sequence = [1,1,6]

    print(find_sequence(root, sequence))
