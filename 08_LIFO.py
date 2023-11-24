## --------- 문제 ---------
# 매일의 온도를 나타내는 정수형 배열 temperatures가 주어진다. 
# answer 배열의 원소 answer[i]는 i번째 날의 온도보다 더 따뜻해지기까지 며칠을 기다려야 하는지 나타낸다
# 만약 더 따뜻해지는 날이 없다면 answer[i] == 0이다. answer 배열을 반환하는 함수를 구현해라

def dailyTemperature(temperatures) : 
    # answer 배열 0으로 초기화
    ans = [0] * len(temperatures)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures) :
        while stack and stack[-1][1] < cur_temp :
        # 스택이 비어있지 않고, 스택의 top의 온도가 현재 온도보다 낮을 경우
            prev_day, prev_temp = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    return ans

print(dailyTemperature([73, 74, 75, 71, 69, 72, 76, 73]))
