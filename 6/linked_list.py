from copy import deepcopy

class Node: # dataclass
    def __init__(self, value, next) -> None:
        self.value = value
        self.next = next
    
    def __str__(self) -> str:
        return str(self.value)

class NoItemError(Exception):
    pass

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.len = 0
    
    def __str__(self) -> str:
        result = ""

        node = self.head
        while node is not None:
            result += str(node)
            result += " "
            node = node.next

        return result
    
    def __len__(self) -> int:
        count = 0
        node = self.head
        while node is not None:
            node = node.next
            count += 1
        
        return count
    
    def __contains__(self, value) -> bool:
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        
        return False

    def push_front(self, value):
        node = Node(value, self.head)
        self.head = node
        self.len += 1
    
    def pop_front(self):
        if self.head is None:
            raise NoItemError
        node = self.head
        self.head = node.next
        self.len -= 1
        return node.value
    
    def __iter__(self):
        return deepcopy(self)
    
    def __next__(self):
        if self.head is None:
            raise StopIteration
        return self.pop_front()

if __name__ == "__main__":
    ll = LinkedList()
    print(ll, ", ", len(ll))
    ll.push_front(1)
    print(ll, ", ", len(ll))
    ll.push_front(2)
    print(ll, ", ", len(ll))
    ll.pop_front()
    print(ll, ", ", len(ll))
    ll.pop_front() # ここで空になる
    ll.push_front(1)
    ll.push_front(2)
    ll.push_front(3)
    ll.push_front(4)
    print(3 in ll)
    print(4 in ll)
    # ll.pop_front() # 空のリストからpop -> Error
    print(ll)
    for i in ll:
        print(i)
    print(ll, len(ll))