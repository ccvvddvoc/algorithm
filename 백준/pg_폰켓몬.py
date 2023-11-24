
def solution(nums) : 
    total_cnt = int(len(nums)/2)
    nums_set = set(nums)

    if total_cnt > len(nums_set) :
        return (len(nums_set))
    else : 
        return (total_cnt)