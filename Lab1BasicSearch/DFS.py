graph = { 
'A' : ['B','C'], 
'B' : ['D', 'E'], 
'C' : ['F'], 
'D' : [], 
'E' : ['F'], 
'F' : [] 
} 
def DFS( graph,start, end):
   
    # # them start vao mang path
    # path.append(start)
    # # noi mang path va mang neighbor cua start 
    # path.extend( graph[start])
    # # neu path khac rong va top(path) khong la dich
    # while path & path.index()!=end:
    #     if len(graph[path.index()])==0:
    #         path.pop(0)
    #     else:
    #         for member in len(graph[path.index()]):
    #             path.pop(member)
    #     return "complete"
    # khoi tao 
    path=[]
    stack=[]
    path.append(start) 
    # them start vao path, them neighbor cua start vao stack
    stack.append(graph[start])
    # neu khong con neighor quay lại vi tri gan nhat cua stack tiep tuc lay neighbor khac
    while path & path.index()!=end:
        path.append(stack.pop())
        

DFS(graph ,'A','D')     