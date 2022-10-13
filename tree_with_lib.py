from anytree import Node, RenderTree, AsciiStyle, find_by_attr
f = Node("f")
b = Node("b", parent=f)
a = Node("a", parent=b)
d = Node("d", parent=b)
c = Node("c", parent=d)
e = Node("e", parent=d)
g = Node("g", parent=f)
i = Node("i", parent=g)
h = Node("h", parent=i)
print(RenderTree(f, style=AsciiStyle()).by_attr())
print(find_by_attr(f, "d"))



