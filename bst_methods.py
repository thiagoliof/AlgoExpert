# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
from turtle import right


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

        if value < self.value:
            if not self.left is None:
                self.left.remove(value, self)
        elif value > self.value:
            if not self.right is None:
                self.right.remove(value, self)
        
        else:
            if not self.left is None and not self.right is None:
                self.value = self.right.getMinValue()
            # root tree
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
        
    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()

    def getMaxValue(self):
        if self.right is None:
            return self.value
        else:
            return self.right.getMaxValue()



    
            



if __name__ == "__main__":
    bst = BST(20)
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
    
    var = bst.remove(20)
    print(var)

    max = bst.getMaxValue()
    print(max)

    

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
    
    
