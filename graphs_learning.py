from collections import deque

graph = {
    "a": ["b", "c", ],
    "b": ["d"],
    "c" : ["e"],
    "d" : ["f"],
    "e" : [],
    "f" : []
}

# lembrando que depthfirst usa stack, 
# e ele busca uma travessia de profundidade
def depthfirst(graph, initial_node):
    stack = []
    stack.append(initial_node)
    
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)

# agora com recursividade
def depthfirst_recursion(graph, source):
    print(source)
    for neighbor in graph[source]:
        depthfirst_recursion(graph, neighbor)


# breadth utilizamos uma queue
def breadthfirst(graph, source):
    queue = deque([source])
    while queue:
        current = queue.popleft()
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


graph_has_path = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": [] 
}

def has_path_depth_first(g, source, dst):
    if source == dst:
        return True
     
    for neighbor in g[source]:
        if has_path_depth_first(g, neighbor, dst) == True:
            return True
    
    return False
    
def has_path_breadth_first(graph, source, dst):
    queue = deque([source])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    
    return False

if __name__ == "__main__":
   #has_path = has_path_depth_first(g=graph_has_path, source="f", dst="k")
   #print(has_path)
    depthfirst(graph, "a")
    # print("fim depthfirst ---------------------------")
    # depthfirst_recursion(graph, "a")
    # print("fim depthfirst_recursion ---------------------------")
    # breadthfirst(graph, "a")
    # print("fim breadthfirst ---------------------------")