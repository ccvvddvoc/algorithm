# 정수가 저장된 배열 nums가 주어졌을 때, nums의 원소중 두 숫자를 더해서 target이 될 수 있으면 
# True, 불가능하면 False를 반환해라. 같은 원소는 두번 사용할 수 없다

# 접근 방법 : 
# 완전탐색 시  -> O(n^2)
# 정렬 하였을 경우 n*log(n) 사용

# 1) 딕셔너리에 nums 배열의 값들을 key값으로 저장
# 2) 배열을 돌면서 target - 현재 값이 딕셔너리에 있다면 return True

nums = [4,1,9,7,5,3,16]
target = 14

def solution(nums, target) : 
    nums_dict = {} # 딕셔너리 선언
    
    for i in nums : # 딕셔너리 키값 채움
        nums_dict[i] = 0

    for i in nums : # 딕셔너리의 키값과 nums 배열의 값을 사용하여 계산
        n = target - i 
        if ((n in nums_dict) & (n != i)) :
            return True
    return False

print(solution(nums, target))

