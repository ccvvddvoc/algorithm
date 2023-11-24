# 그래프 순회 :
# - 그래프 탐색이라고도 부르며, 그래프의 각 정점을 방문하는 과정을 말한다.
# - 깊이 우선 탐색(DFS), 너비 우선 탐색(BFS) 

from collections import deque

# 인접 리스트 구현 방식
graph = {
    'A' : ['B', 'D', 'E'],
    'B' : ['A', 'C', 'D'],
    'C' : ['B'],
    'D' : ['A', 'B'],
    'E' : ['A']
}

# 너비 우선 탐색 -> 시작점에서 가장 가까운 곳부터 방문
def bfs(graph, start_v) :
    visited = [start_v]
    queue = deque(start_v)
    while queue :
        cur_v = queue.popleft()
        for v in graph[cur_v] :
            if v not in visited :
                visited.append(v)
                queue.append(v)
    return visited

print(bfs(graph, 'A'))