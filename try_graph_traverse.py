from locale import currency
import queue


def depthfirst_no_recursion(graph, source):
    stack = []
    stack.append(source)

    while len(stack) > 0:
        current = stack.pop()
        print('current', current)
        for neighbor in graph[current]:
            print('neighbor:', neighbor)
            stack.append(neighbor)



def depth_with_recursion(graph, source):
    print('current', source)
    for neighbor in graph[source]:
        depth_with_recursion(graph, neighbor)
   
        

from collections import deque
def breadth_first(graph, source):
    queue = deque()
    queue.append(source)

    while queue:
        current = queue.popleft()
        print('current', current)
        for neighbor in graph[current]:
            print('neighbor', neighbor)
            queue.append(neighbor)




graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c" : ["e"],
    "d" : ["f"],
    "e" : [],
    "f" : []
}


if __name__ == "__main__": 
    breadth_first(graph, 'a')
    

