# 땅 고르기 : 땅의 높이를 모두 동일하게 만드는 작업
# 세로 N, 가로 M 크기의 집터, 집터 맨 왼쪽 위 좌표는 (0,0)
# 땅 고르기를 하는 것이 목적

# 1) 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣음 -> 2초
# 2) 인벤토리에서 블록 하나를 꺼내어 (i, j)의 가장 위에 있는 블록 위에 놓는다 -> 1초

# 작업에 걸리는 최소 시간, 땅의 높이를 출력
# 인벤토리 내의 블록의 수 : B
# 땅의 높이는 0 이상이며, 256을 초과할 수 없음

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

# 딕셔너리에 좌표를 키로 하여, 높이를 저장
# 반복문을 돌면서 dict.values() 리스트 내의 모든 원소가 같다면 종료
# dict.values()로 최대 높이, 최소 높이를 변수에 저장
# 박스의 수를 고려하여, 최대 높이에 맞추는 시간, 최소 높이에 맞추는 시간을 계산하여 
# 최소인 것으로 선택하여 출력한다

# 반복문 돌면서 입력 받기

land = []
for i in range(N) :
    l = list(map(int, input().split()))
    land.extend(l)

land_dict = {}
for i, h in enumerate(land) : 
    land_dict[i] = h

max_height = max(land_dict.values())
min_height = min(land_dict.values())

# 최대 높이를 맞출 때 :
# 추가로 박스를 쌓아야 하니까 원래 박스 수에서 마이너스를 해주어야 함
# 반복문을 돌면서 높이 쌓아줌
# 박스 수가 음수가 되거나, 크기가 같아지면 반복문 종료

def find_max(land, max_height, N, M, B) : 
    time = 0
    for ind, i in enumerate(land) : 
        while (1) : 
            if (B < 0) :
                return 0, 0 
            if (i == max_height) :
                break
            else : 
                i += 1
                B -= 1
                time += 1
        land[ind] = i
    return time, max(land)


def find_min(land, min_height, N, M, B) : 
    time = 0
    for ind, i in enumerate(land) : 
        while (1) : 
            if (i == min_height) : 
                break
            else : 
                i -= 1
                B += 1
                time += 2
        land[ind] = i
    return time, max(land)

# print(find_max(land, max_height, N, M, B))
print(find_min(land, min_height, N, M, B))


