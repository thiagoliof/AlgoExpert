# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value, isRoot=False):
        self.value = value
        self.left = None
        self.right = None
        self.root = isRoot

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
            
        return self

    def contains(self, value):
        # Write your code here.
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True
    

    def remove(self, value, parent=None):
        obj = None
        if value < self.value:
            if not self.left is None:
                self.left.remove(value, self)
        elif value > self.value:
            if not self.right is None:
                self.right.remove(value, self)
        elif value == self.value:
            obj = self

        return obj




    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()
            



if __name__ == "__main__":
    bst = BST(20, True)
    bst.insert(10)
    bst.insert(9)
    bst.insert(8)
    bst.insert(11)
    bst.insert(12)
    bst.insert(30)
    bst.insert(29)
    bst.insert(39)
    bst.insert(36)
    bst.insert(35)
    bst.insert(34)
    
    var = bst.remove(34)
    print(var)


    

"""
    20
  /
 0
  \
   1
    \
     2
      \
       3  
"""
    
    
