# num_list = [3,4,5,2,5,4,6,7,3,7,2,2,1]
num_list = [2,3,4,5]

def solution(num_list):
    answer = 0
    if (len(num_list) >= 11) :
        for num in num_list :
            answer += num
    elif (len(num_list) <= 10) :
        answer = 1 
        for num in num_list :
            answer *= num
    return answer

print(solution(num_list))