import unittest
import collections

arr_to_iterate = [
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

def transforArr(arr):
    rows = len(arr)
    cols = len(arr[0])
    
    for r in range(0, rows):
        for c in range(0, cols):
            if r == c:
                arr_to_iterate[r][c] = 1
            

visited = set()

def surounding(row, col, p="*"):
    q = collections.deque()
    item = []
    item.append([row, col])

    directions = [
                    [-1, 0], #cima, 
                    [1, 0], # baixo, 
                    [0, -1], # esquerda
                    [0, 1], #direita
    ]

    while len(item) > 0:
        
        current = item.pop()
        r, c = current

        for dr, dc in directions:
            _r = r + dr
            _c = c + dc
            if ((_r, _c) not in visited 
            and _r in range(rows) 
            and _c in range(cols)):
                visited.add((_r, _c))
        


def number_of_islands(arr):
    global rows, cols
    rows = len(arr)
    cols = len(arr[0])
    islands = 0

    for r in range(0, rows):
        for c in range(0, cols):
            if arr[r][c] == 1 and (r, c) not in visited:
                surounding(r, c)
                islands += 1
    
    return islands
                


def transforArrDiagonalSuperiorDireita(arr):
    
    rows_lenght = len(arr)
    cols_lenth = len(arr[0])
    
    stack = []
    cidx = 1
    for r in range(0, rows_lenght):
        for c in range(0, cols_lenth):
            if r not in stack:
                arr_to_iterate[r][cols_lenth-(cidx)] = "x"
                cidx = cidx + 1
                stack.append(r)
            
            
            
            
[
    [0, 0, 0, 0, 'x'], 
    [0, 0, 0, 'x', 0], 
    [0, 0, 'x', 0, 0], 
    [0, 'x', 0, 0, 0], 
    ['x', 0, 0, 0, 0]
]
            

            
            
            

            
        
 




if __name__ == "__main__":
    n = transforArrDiagonalSuperiorDireita(arr_to_iterate)
    print(arr_to_iterate)

[
    [0, 0, 0, 0, 1], 
    [0, 0, 0, 1, 0], 
    [0, 0, 1, 0, 0], 
    [0, 1, 0, 0, 0], 
    [1, 0, 0, 0, 0]
]