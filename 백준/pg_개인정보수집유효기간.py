# 오늘 날짜로 파기해야 할 개인정보 번호들을 구해야 하며,
# 모든 달은 28일 까지 있다고 가정한다

# 오늘 날짜 : 2022년 5월 19일 일때, 
# A : 6달
# B : 12달
# C : 3달

# 1) 2021.05.02 ~ 2021.11.01 -> 2021.11.02부터 폐기
# 2) 2021.07.01 ~ 2022.06.28 -> 2022.07.01부터 폐기
# 3) 2022.02.19 ~ 2022.05.18 -> 2022.05.19부터 폐기
# 4) 2022.02.20 ~ 2022.05.19 -> 2022.05.20부터 폐기

today = "2020.01.01"	
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

limit = []
term_dict = {}

for t in terms : 
    term, month = t.split()
    term_dict[term] = month

year, month, day = map(int, today.split('.'))
today = year*336 + month*28 + day

for i, p in enumerate(privacies) : 
    times, term = p.split()
    year, month, day = map(int, times.split('.'))
    limit_day = year*336 + month*28 + day + int(term_dict[term])*28-1
    if today > limit_day :
        limit.append(i+1)

print(limit)
