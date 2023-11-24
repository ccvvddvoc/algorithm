class Node : 
    def __init__(self, value=0, next=None) :
        self.value = value
        self.next = next

class LinkedList(object) :
    def __init__(self) :
        self.head = None
        self.tail = None
    
    def append(self, value) : # tail을 사용하여 시간복잡도 O(1)
        new_node = Node(value)
        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else : 
            self.tail.next = new_node
            self.tail = new_node

    def print_all_value(self) :
        current = self.head
        while (current != self.tail) :
            print(current.value)
            current = current.next
        print(self.tail.value)


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.print_all_value()