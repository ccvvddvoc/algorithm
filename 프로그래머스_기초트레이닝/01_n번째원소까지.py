
temp = [73, 74, 75, 71, 69, 72, 76, 73]

def solution(temp) :
    
    stack = [(0, temp[0])] # 첫번째 원소를 넣고
    answer = [0] * len(temp)

    
    for temp_i in range(1, len(temp)) :
        
        while (stack and stack[-1][1] < temp[temp_i]) :
            answ_i, answ_t = stack.pop()
            answer.append(temp_i-answ_i)
        stack.append((temp_i, temp[temp_i]))
    
    while stack :
        answer.append(0)
    return answer


print(solution(temp))
   
