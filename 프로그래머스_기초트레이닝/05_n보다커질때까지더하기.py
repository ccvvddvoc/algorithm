# numbers = [34, 5, 71, 29, 100, 34]; n=123
numbers = [58, 44, 27, 10, 100]; n=139
def solution(numbers, n):
    answer = 0
    for  number in numbers :
        if answer > n : 
            break
        answer += number
    return answer

print(solution(numbers, n))