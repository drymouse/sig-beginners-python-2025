from linked_list import Node, LinkedList

class MyList(LinkedList):
    def __str__(self) -> str:
        result = "["

        node = self.head
        while node is not None:
            result += str(node)
            if node.next is not None:
                result += ", "
            node = node.next

        result += "]"
        return result
    
    def __inode(self, index):
        node = self.head
        while node is not None and index > 0:
            node = node.next
            index -= 1
        
        return node
    
    def __getitem__(self, index):
        node = self.__inode(index)
        if node is None:
            raise IndexError
        return node.value
    
    def __setitem__(self, index, value):
        node = self.__inode(index)
        if node is None:
            raise IndexError
        node.value = value

    def __delitem__(self, index):
        if index == 0:
            if self.head is None:
                raise IndexError
            self.head = self.head.next
            self.len -= 1
            return
        node = self.__inode(index - 1)
        if node is None or node.next is None:
            raise IndexError
        node.next = node.next.next
        self.len -= 1
    
    def insert(self, index, value):
        if index == 0:
            self.push_front(value)
            return
        node = self.__inode(index - 1)
        if node is None:
            raise IndexError
        new_node = Node(value, node.next)
        node.next = new_node
        self.len += 1

    def append(self, value):
        self.insert(self.len, value)
    
if __name__ == "__main__":
    lst = MyList()
    lst.push_front(1)
    lst.push_front(2)
    lst.push_front(3)
    lst.push_front(4)
    print(lst)
    print(lst[0])
    print(lst[2])
    # print(lst[4])
    lst[1] = 100
    print(lst)
    del lst[1]
    print(lst)
    del lst[0]
    print(lst)
    lst.insert(1, 100)
    print(lst)
    lst.insert(0, 101)
    print(lst)
    lst.append(1000)
    lst.append(1001)
    lst.append(1002)
    print(lst)
