## 코테 적용 방법
# Linked List의 다양한 활용
# - 선형 자료구조 + 중간에 데이터 추가/삭제 용이
# - Tree or Graph에 활용

## Step1 문제 이해하기 Tip
# 1) 입력, 출력 확인
# - 입력 값의 특징 (정수? 값 크기 범위? 마이너스 가능? 소수?)
# - 출력 값의 특징 (어떤 값을 반환해야하나, 정해진 형식대로 반환하려면 어떻게 구현해야 할까)
# 2) 입력값의 size 확인
# - 시간복잡도를 계산하기 위해 size확인
# 3) 제약조건 확인
# - 시간복잡도 제한 확인, 알고리즘을 무엇을 선택해야 할지
# 4) 예상가능한 오류 파악
# - 상황을 가정하면서 오류를 예상
# - 입력값의 범위, stack overflow 등

## --------- 문제 ------------
# 인터넷 브라우저의 방문기록과 동일한 작동을 하는 browser history class를 구현할 것이다
# BrowserHistory(string hompage)를 호출하면 브라우저는 홈페이지에서 시작이 된다
# void visit(string url)을 호출하면 현재 page의 앞에 있는 페이지기록은 다 삭제가 되고, url로 방문한다
# string back(int steps)를 호출하면 steps수 만큼 뒤로 가기를 한다.
# string forward(int steps)를 호출하면 steps수 만큼 앞으로 가기를 한다.

## --------- 제약조건 ------------
# 1 <= homepage.length <= 20
# 1 <= url.length <= 20
# 1 <= step <= 100
# homepage와 url은 '.'을 포함한 영어 소문자로 구성되어있다
# visit, back, forward는 최대 5000번의 호출이 있을 수 있다


## -------- Linked List 구현 ----------

class Node(object) :
    def __init__(self, url, next=None, prev=None) :
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory(object) :
    def __init__(self, homepage) :
        self.head = self.current = Node(url=homepage)
    
    def visit(self, url) :
        self.current.next = Node(url=url, prev=self.current)
        self.current = self.current.next 

    def back(self, steps) :
        for i in range(steps) :
            if (self.current.prev) :
                self.current = self.current.prev
            else :
                break
        return self.current.url

    def forward(self, steps) :
        for i in range(steps) :
            if (self.current.next) :
                self.current = self.current.next
            else :
                break
        return self.current.url
    
bh = BrowserHistory("leetcode.com")
bh.visit('google.com')
bh.visit('facebook.com') 
bh.visit('youtube.com')
print(bh.back(1))
print(bh.back(1))
print(bh.forward(1))
bh.visit('linkedin.com')
print(bh.forward(2))
print(bh.back(2))
print(bh.back(7))
