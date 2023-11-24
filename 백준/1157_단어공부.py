
import sys

input = sys.stdin.readline

# word = input()
word = 'zZa'.upper()

word_dict = {}

for w in word : 
    # 이미 키가 있는 경우
    if w in word_dict : 
        word_dict[w] += 1
    else : 
        word_dict[w] = 0 

max_cnt = 0 
max_num = max(list(word_dict.values()))

for w in word_dict : 
    if (word_dict[w] == max_num) : 
        max_cnt += 1
        max_key = w

if (max_cnt < 2) : 
    print(max_key)
else : 
    print('?')






