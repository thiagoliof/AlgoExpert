def minHeightBst(array):
    return minHeightBstHelper(array, None, 0, len(array) - 1)

def minHeightBstHelper(array, bst, startidx, endIdx):
    if endIdx < startidx:
        return
    mididx = (startidx + endIdx) // 2
    value_to_add = array[mididx]
    if bst is None:
        bst = BST(value_to_add)
    else:
        bst.insert(value_to_add)

    minHeightBstHelper(array, bst, startidx, mididx-1)
    minHeightBstHelper(array, bst, mididx + 1, endIdx)
    return bst
    

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


if __name__ == "__main__":
    arr = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    bst = minHeightBst(arr)
    a = 'a'
