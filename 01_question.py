## 1) 문제 이해
## 2) 접근 방법
## 3) 코드 설계 
## 4) 코드 구현

# ----------- 문제 -----------
# 정수가 저장된 배열 nums가 주어졌을 때, nums의 원소중 두 숫자를 더하여 
# target이 될 수 있으면 True, 불가능하면 False를 반환해라. 같은 원소를 두번 사용할 수 없다
# input : nums = [4,1,9,7,5,3,16], target=14
# output : True

# ----------- 제약조건 -----------
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9

# ----------- 접근방법 -----------
# - 직관적으로 생각 (완전탐색, 문제상황을 단순화, 극한화하여 생각)
# - 자료구조와 알고리즘 활용 (어떠한 자료구조를 사용할지 결정, 자료구조에 따른 알고리즘을 적용)
# - 메모리 사용 (시간복잡도를 줄이기 위해 메모리를 사용하는 방법. ex.해시테이블)

nums = [4,1,9,7,5,3,16]
# nums = [2,1,5,7]
target = 14

# def twoSum(nums, target) :
#     n = len(nums)
#     for i in range(n-1) : 
#         for j in range(i+1, n) : 
#             if nums[i] + nums[j] == 14 : 
#                 return True
#     return False
# print(twoSum(nums, target))

# + Sort, two pointer
def twoSum(nums, target) :
    nums.sort()
    i, j  = 0, len(nums)-1
    while i<j :
        # 두 숫자의 합이 타겟보다 더 큰 경우
        if (nums[i] + nums[j] > target) :
            j -= 1
        # 두 숫자의 합이 타겟보다 작은 경우
        elif (nums[i] + nums[j] < target) :
            i += 1
        # 두 숫자의 합이 타겟과 같은 경우 
        elif (nums[i] + nums[j] == target) :
            return True
    return False

print(twoSum(nums, target))
