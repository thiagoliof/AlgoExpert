class Node:
    # Constructor to create a new Node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
# A utility function to check if a given node is leaf or not
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False
 
# This function return sum of all left leaves in a
# given binary tree
def leftLeavesSum(root):
 
    # Initialize result
    res = 0
     
    # Update result if root is not None
    if root is not None:
 
        # If left of root is None, then add key of
        # left child
        if isLeaf(root.left):
            res += root.left.key
        else:
            # Else recur for left child of root
            res += leftLeavesSum(root.left)
 
        # Recur for right child of root and update res
        res += leftLeavesSum(root.right)

    return res
 
# Driver program to test above function
 
# Let us construct the Binary Tree shown in the above function
root = Node(20)
root.left = Node(9)
#root.left.left = Node(10)
# root.left.left = Node(10)
#root.right = Node(49)
#root.right.left = Node(1)         
print ("Sum of left leaves is", leftLeavesSum(root))
 