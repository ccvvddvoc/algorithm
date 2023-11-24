# 노드 구현
class Node : 
    def __init__(self, value=0, next=None) :
        self.value = value
        self.next = next
# # 노드 생성
# first = Node(value=1)
# second = Node(value=2)
# third = Node(value=3)

# # 노드 연결
# first.next = second
# second.next = third

# Linked List 구현
class LinkedList(object) : 
    def __init__(self) : 
        self.head = None
    
    def append(self, value) : # 시간복잡도 O(n)
        new_node = Node(value)
        if (self.head is None) : # 첫 노드가 생겼을 경우, head는 new_node를 가리킴 
            self.head = new_node
        else : # 첫 노드부터 마지막까지 연결 
            current = self.head
            while (current.next) : 
                current = current.next
            current.next = new_node
    
    def get(self, idx) : # 시간복잡도 O(n)
        current = self.head
        for i in range(idx) :
            current = current.next
        return current.value
    
    def insert_at(self, idx, value) : 
        new_node = Node(value)

        if idx == 0 : 
            new_node.next = self.head
            self.head = new_node

        elif idx != 0 :
            current = self.head
            for i in range(idx-1) :
                current = current.next
            new_node.next = current.next
            current.next = new_node
    
    def remove(self, idx) :
        current = self.head 
        
        if idx == 0 : # 제일 처음의 노드를 제거할 경우
            self.head = current.next

        elif idx != 0 : 
            for i in range(idx-1) :
                current = current.next
            temp = current.next
            current.next = temp.next            


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.insert_at(2, 5)

# print(linked_list.get(0))
# print(linked_list.get(1))
# print(linked_list.get(2))
# print(linked_list.get(3))
# 현재 linked_list : 1,2,5,3

linked_list.remove(0)
print(linked_list.get(0))
print(linked_list.get(1))
print(linked_list.get(2))
