
graph1 = {
    's': ['d', 'e', 'p'],
    'a': [],
    'b': ['a'],
    'c': ['a'],
    'd': ['b', 'c', 'e'],
    'e': ['h', 'r'],
    'f': ['c', 'g'],
    'g': [],
    'h': ['p', 'q'],
    'p': ['q'],
    'q': [],
    'r': ['f']
}
graph2 = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'k'],
    'd': ['b', 'e', 'm'],
    'e': ['d', 'm', 'n'],
    'f': ['s', 'p'],
    'g': ['m', 't'],
    'h': ['s', 'k'],
    'k': ['c', 'h'],
    'm': ['d', 'n', 'g'],
    'n': ['e', 'm'],
    'p': ['f', 'q'],
    'q': ['p', 'r'],
    'r': ['q', 't'],
    't': ['r', 'g'],
    's': ['h', 'f']
}
graph3 = {
    'a': ['b', 'c'],
    'b': ['a', 'c', 'd'],
    'c': ['a', 'b', 'd'],
    'd': ['b', 'c', 'e', 'f', 'g'],
    'e': ['d', 'g'],
    'f': ['d', 'g'],
    'g': ['d', 'e', 'f']
}


# DFS with stack
def DFS(graph, start, end):
    print(f'DFS start {start} to {end}:')
    visited = []
    stack = []
    stack.append([start])

    while stack:
        path = stack.pop()

        node = path[-1]
        if node == end:
            return path
        visited.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)


print(DFS(graph1, 's', 'g'))
print(DFS(graph2, 's', 'g'))
print(DFS(graph2, 'a', 'g'))


# DFS with stack, and strategy deep node
def DFSWithStrategy(graph, start, end):
    print(f'DFS start {start} to {end} - with strategy deep node:')
    visited = []
    stack = []
    stack.append([start])

    def getIndexMaxNodeNeighbor(stack):
        maxNodeNeighbor = []
        for stackItem in stack:
            if len(stackItem) > len(maxNodeNeighbor):
                maxNodeNeighbor = stackItem
        return stack.index(maxNodeNeighbor)

    while stack:
        index = getIndexMaxNodeNeighbor(stack)
        path = stack.pop(index)

        node = path[-1]
        if node == end:
            return path
        visited.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)


print(DFSWithStrategy(graph1, 's', 'g'))
print(DFSWithStrategy(graph2, 's', 'g'))
print(DFSWithStrategy(graph3, 'a', 'g'))
