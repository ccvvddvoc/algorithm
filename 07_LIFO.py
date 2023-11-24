## -- stack의 다양한 활용
# - LIFO 특성을 활용한 문제
# - DFS(깊이 우선 탐색)에 사용

## -- 괄호 유효성 문제 --
# (){}[]를 포함하고 있는 문자열 s가 주어졌을 때, 괄호가 유효한지 아닌지 판별하시오

## -- 제약조건 --
# 1 <= s.length <= 10^4
# s는 ()[]{}의 등의 괄호 들로만 구성되어 있다
def isValid(s) : 
    stack = []
    for p in s :
        if p == '(' :
            stack.append(')')
        elif p == '{' :
            stack.append('}')
        elif p == '[' :
            stack.append(']')
        elif (not stack) or (stack.pop() != p) :
            # not stack : 스택이 비어있으면 True, 비어있지 않으면 False 반환
            # 스택이 비어있는 경우, 닫는 괄호가 들어온다면 False를 출력
            # 스택이 비어있지 않은 경우, pop을 수행하고 들어오는 괄호와 같지 않다면 False출력
            # pop을 수행하고 들어오는 괄호와 같다면 정상동작
            return False
    return not stack

s = "{(([]))[]}}"

print(isValid(s))

            