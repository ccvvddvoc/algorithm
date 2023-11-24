# 완전 탐색 관련 문제는 그래프로 표현할 수 있고,
# DFS, BFS를 사용하면 쉽게 풀 수 있다

## ----- 문제 -----
# 0번방부터 n-1번방까지 총 n개의 방이 있다. 0번 방을 제외한 모든 방은 잠겨있다. 우리의 목표는
# 모든 방에 visit하는 것이다. 하지만 잠겨져있는 방은 key가 없으면 visit할 수 없다. 각 방에 방문할 때,
# 별개의 열쇠뭉치를 찾을 수도 있다. 각각의 열쇠에는 number가 쓰여져 있고, 해당 번호에 해당하는 방을 잠금 해제할 수 있다.
# 열쇠뭉치는 모두 가져갈 수 있고, 언제든 방문을 열기 위해 사용할 수 있다
# 문제에서 rooms 배열이 주어지고, rooms[i]는 해당 방에서 얻을 수 있는 열쇠뭉치 목록을 표현한다.
# 모든 방을 visit할 수 있으면 True, 그렇지 않으면 False를 반환하라 

## ----- 제약조건 ------
# n == rooms.length(방의 수)
# 2 <= n <= 1000 --> O(n^2)이여도 가능하다
# 0 <= rooms[i].length(열쇠의 수) <= 1000 --> 열쇠의 수도 10^6이 될 수 있다
# 1 <= sum(rooms[i].length) <= 3000 --> 열쇠의 수가 최대 3000개 이므로 위의 가정은 X
# 0 <= rooms[i][j] < n --> 방의 키의 숫자는 방의 수를 넘을 수 없다

# - 완전탐색(DFS, BFS)의 시간복잡도 : O(V + E) 
# O(1000 + 3000)이므로 완전탐색 사용 가능 

# def canVisitAllRooms(rooms) :
#     visited = []
    
#     # v에 연결되어있는 모든 vertex에 방문
#     def dfs(v) : 
#         visited.append(v)
#         for next_v in rooms[v] :
#             if next_v not in visited :
#                 dfs(next_v)
#     dfs(0)

#     if len(visited) == len(rooms) : 
#         return True
#     else : 
#         return False
#     # return visited

rooms = [[1,3], [2,4], [0], [4], [], [3,4]]
# rooms = [[1], [2], [3], []]


# print(canVisitAllRooms(rooms))


# ## 풀이 2
# def canVisitAllRooms(rooms) :
#     visited = [False] * len(rooms)

#     def dfs(v) :
#         visited[v] = True
#         for next_v in rooms[v] :
#             if visited[next_v] == False : # O(1)
#                 dfs(next_v)
#     dfs(0)

#     if len(visited) == len(rooms) :
#         return True
#     else :
#         return False


## 풀이 3
from collections import deque

def canVisitAllRooms(rooms) :
    visited = [False] * len(rooms)

    def bfs(v) :
        queue = deque()
        queue.append(v)
        visited[v] = True

        while queue :
            cur_v = queue.popleft()
            for next_v in rooms[cur_v] :
                if visited[next_v] == False : 
                    queue.append(next_v)
                    visited[next_v] = True
    bfs(0)

    return all(visited)
                

print(canVisitAllRooms(rooms))




