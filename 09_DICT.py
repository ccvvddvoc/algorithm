score = {
    'math' : 97,
    'eng' : 49,
    'kor' : 89
}

print(score['math'])

# 수정
score['math'] = 77
print(score['math'])

# 추가
score['sci'] = 100
print(score['sci'])

# 딕셔너리 내 키가 있는지 검색 : in -> 시간복잡도 O(1), set도 O(1), 리스트도 가능하지만 O(n)
print('music' in score) # 없는 경우
print('sci' in score) # 있는 경우

if 'music' in score : 
    print(score['music'])
else :
    score['music'] = 0

