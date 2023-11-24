

graph = {
    'A' : ['B', 'D', 'E'],
    'B' : ['A', 'C', 'D'],
    'C' : ['B'],
    'D' : ['A', 'B'],
    'E' : ['A']
}

# def dfs(graph, cur_v, visited=[]) :
#     visited.append(cur_v)
#     for v in graph[cur_v] :
#         if v not in visited :
#             visited = dfs(graph, v, visited)
#     return visited
# dfs(graph, 'A')


# 조금 더 단순화 된 코드
# graph = {...}
visited = []

def dfs(cur_v) :
    visited.append(cur_v) 
    for v in graph[cur_v] :
        if v not in visited :
            dfs(v)

dfs('A')
print(visited)

