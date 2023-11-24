##  ------ 문제 ------
# 정렬되어 있지 않은 정수형 배열 nums가 주어졌다. nums 원소를 가지고 만들 수 있는 가장 긴 
# 연속된 수의 갯수는 몇개인지 반환하시오.

## ------ 제약조건 ------
# 0 <= nums.length <= 10^5 --> O(n^2)으로 풀 수 없음, nums 배열은 비어있을 수 있고 이에 대한 대처 필요
# -10^9 <= nums[i] <= 10^9
 
## input & output 
# nums = [100, 4, 200, 1, 3, 2] -> 4
# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] -> 9

nums = [-1, 0, 1, 4, 5, 6, 7, 8, 9]

def longestConsecutive(nums) : 
    longest = 0
    # 딕셔너리에 배열의 값 저장
    nums_dict = {}

    for num in nums : 
        nums_dict[num] = 0 
    
    for num in nums_dict : 
        # 연속된 수의 그룹 중 가장 작은 수를 찾고, 그때만 반복문 실행
        if num - 1 not in nums_dict : 
            cnt = 1
            target = num + 1
            while target in nums_dict :
                target += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

print(longestConsecutive(nums))

