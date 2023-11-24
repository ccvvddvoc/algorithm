## ----- 문제 -----
# grid는 '1' (land)과 '0' (water)으로 이루어진 지도를 표현하는 m,n 이차원 배열이다.
# 이 지도에 표시된 섬들의 총 갯수를 반환하시오
# 섬이란 수평과 수직으로 땅이 연결되어 있고 주변은 물로 둘러쌓여있는 것을 말한다. 
# 또한, grid의 네개의 가장자리는 모두 물로 둘러쌓여있다고 가정하고 문제를 해결하라

## ----- 제약조건 -----
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300 --> 최대 배열에 90000개가 들어갈 수 있다. 10^5이라고 생각하면 O(N^2)의 풀이로는 풀 수 없다
# grid[i][j] is '0'  or '1'



## bfs 사용

from collections import deque

def numIslands(grid) :
    number_of_islands = 0
    m = len(grid)
    n = len(grid[0])
    visited = [[False]*n for _ in range(m)]

    def bfs(x, y) : 
        dx = [-1, 1, 0, 0] # 상하좌우 이동량
        dy = [0, 0, -1, 1]  

        visited[x][y] = True # 방문했다고 표시
        queue = deque()
        queue.append((x,y))
        while queue : 
            cur_x, cur_y = queue.popleft()
            for i in range(4) :
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if (next_x >= 0) & (next_x < m) & (next_y >=0) & (next_y < n) :
                    if (grid[next_x][next_y] == '1' and not visited[next_x][next_y]) :  
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))
                
    for i in range(m) :
        for j in range(n) :
            if (grid[i][j] == '1') & (not visited[i][j]) :
                bfs(i,j)
                number_of_islands += 1

    return number_of_islands

print(numIslands(grid = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
]))