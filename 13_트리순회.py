from collections import deque

def bfs(root) : 
    visited = [] # 방명록
    if root is None :
        return []
    q = deque()
    q.append(root)
    while q : # 큐가 비어있지않는 동안 
        cur_node = q.popleft() # 접근
        visited.append(cur_node.value) # 방문

        if cur_node.left : 
            q.append(cur_node.left) # 접근 예약
        if cur_node.right : 
            q.append(cur_node.right) # 접근 예약
    return visited
