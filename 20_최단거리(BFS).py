## ----- 문제 ------
# n x n 이차원 행렬인 grid가 주어졌을 때, 출발지에서 목적지까지 도착하는 가장 빠른 경로의 길이를 반환하시오
# 만약 경로가 없다면 -1을 반환하시오

# 출발지 : top-left cell, 목적지 : bottom-right cell
# 0인 cell만 지나갈 수 있다
# cell끼리는 8가지 방향으로 연결되어 있다
# 연결된 cell을 통해서만 지나갈 수 있다

## ----- 제약조건 ------
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100 --> BFS의 시간복잡도는 vertex의 개수와 같음 vertex의 수는 n^2이므로 최대 10^4이기 때문에 BFS 사용 가능
# grid[i][j] is 0 or 1

from collections import deque

def shortestPathBinaryMatrix(grid) :
    shortest_path_len = -1
    n = len(grid)

    if grid[0][0] == 1 or grid[n-1][n-1] == 1  : # 출발지와 목적지가 1인 경우 바로 -1 반환
        return shortest_path_len

    visited = [[False]*n for _ in range(n)]
    deltas = [(1,0), (-1,0), (0,-1), (0,1), # 상하좌우
                (1,1), (1,-1), (-1,1), (-1,-1)] # 대각선

    queue = deque()
    queue.append((0,0,1)) # 1 : 길이 정보
    visited[0][0] = True

    while queue : 
        cur_r, cur_c, cur_path_len = queue.popleft()
        # 목적지에 도착했을 경우 cur_path_len을 shortest_path_len에 저장
        if cur_r == n -1 and cur_c == n -1 : 
            shortest_path_len = cur_path_len
            break 

        # 연결되어있는 vertex 확인
        for delta in deltas :
            next_r = cur_r + delta[0]
            next_c = cur_c + delta[1]

            if next_r >= 0 and next_r < n and next_c >=0 and next_c < n :
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c] : # 0일때 통과가능
                    queue.append((next_r, next_c, cur_path_len+1))
                    visited[next_r][next_c] = True

    return shortest_path_len
grid = [[0,0,0], [1,1,0], [1,1,0]]
print(shortestPathBinaryMatrix(grid))