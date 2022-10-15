class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# A function to do preorder tree traversal
arr = []
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        arr.append(root.val)
   
    return arr
 
 
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Preorder traversal of binary tree is")
a = printPostorder(root)
print(a)