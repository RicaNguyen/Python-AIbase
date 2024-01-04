# graph = { 
# 'A' : ['B','C'], 
# 'B' : ['D', 'E'], 
# 'C' : ['F'], 
# 'D' : [], 
# 'E' : ['F'], 
# 'F' : [] 
# } 
# visited =[]
# queue =[]
# def BFS(visited,graph,start, end):
#     queue.append(start)
#     while queue:
#         s=queue.pop(0)
#         print(s, end=' ')
#         if s==end:
#             return
#         visited.append(s)
#         for neighbor in graph[s]:
#             if neighbor not in visited:
#                 queue.append(neighbor)
    
# BFS(visited,graph,'A','E')
#########################################
graph = { 
        '1': ['2', '3', '4'], 
        '2': ['5', '6'], 
        '5': ['9', '10'], 
        '4': ['7', '8'], 
        '7': ['11', '12'] 
        } 
graph1 = {
    's': ['d', 'e', 'p'],
    'a': [],
    'b': ['a'],
    'c': ['a'],
    'd': ['b','c','e'],
    'e': ['h', 'r'],
    'f': ['c', 'g'],
    'g': [],
    'h': ['p', 'q'],
    'p': ['q'],
    'q': [],
    'r': ['f']
}
graph2={
    'a':['b', 'c'], 
    'b':['a','d'],
    'c':['a','k'],
    'd':['b','e','m'],
    'e':['d','m','n'],
    'f':['s','p'],
    'g':['m','t'],
    'h':['s','k'],
    'k':['c','h'],
    'm':['d','n','g'],
    'n':['e','m'],
    'p':['f','q'],
    'q':['p','r'],
    'r':['q','t'],
    't':['r','g'],
    's':['h','f']
}
graph3={
    'a':['b', 'c'],
    'b':['a','c','d'],
    'c':['a','b','d'],
    'd':['b','c','e','f','g'],
    'e':['d','g'],
    'f':['d','g'],
    'g':['d','e','f']
}
def bfs(graph, start, end):
    visited =[]
    queue= []
    queue.append([start])
    while queue:
        path=queue.pop()
        node =path[-1] 
        if node==end:
            return path
        visited.append(node)
        for neighbour in graph.get(node, []): 
            if neighbour not in visited: 
                new_path = list(path) 
                new_path.append(neighbour) 
                queue.append(new_path)

print (bfs(graph, '1', '11')) 
print (bfs(graph2, 'a', 'g'))
print (bfs(graph3, 'a', 'g'))