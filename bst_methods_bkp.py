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
        # Write your code here.
        # Do not edit the return statement of this method.
        
        # primeiro verifica se é maior ou menor
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        # -------------------------------------------------        
        # essa primeira parte do algoritimo verifica
        # se é maior ou menor, ou seja, aqui de fato 
        # não tem exclusão.
        
        
        
        else:

            # esse primeiro if verifica se o item que deu match
            # tem uma saida pro lado esquerdo e uma pro lado direito
            # ou seja, nesse ponto temos uma bifuração
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            
            ## aqui é quando vamos tirar o root node
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

        return self

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
    
    bst.remove(34)


    

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
    
    
