from linked_list import Node, LinkedList

class DictTuple:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
    
    def __str__(self):
        return repr(self.key) + ": " + repr(self.value)

class MyDict(LinkedList):
    def __str__(self) -> str:
        result = "{"

        node = self.head
        while node is not None:
            result += str(node)
            if node.next is not None:
                result += ", "
            node = node.next

        result += "}"
        return result
    
    def __getitem__(self, key):
        node = self.head
        while node is not None:
            if node.value.key == key:
                return node.value.value
            node = node.next
        raise KeyError
    
    def __setitem__(self, key, value):
        node = self.head
        while node is not None:
            if node.value.key == key:
                node.value.value = value
                return
            node = node.next
        tpl = DictTuple(key, value)
        self.push_front(tpl)
    
    def __delitem__(self, key):
        prev = None
        node = self.head
        while node is not None:
            if node.value.key == key:
                if prev is None:
                    self.head = node.next
                else:
                    prev.next = node.next
                return
            prev = node
            node = node.next
        
        raise KeyError

    def __next__(self):
        if len(self) == 0:
            raise StopIteration
        return self.pop_front().key
    
    def __contains__(self, value) -> bool:
        node = self.head
        while node is not None:
            if node.value.key == value:
                return True
            node = node.next
        
        return False

if __name__ == "__main__":
    dct = MyDict()
    dct["apple"] = "ringo"
    dct["banana"] = "banana"
    dct["cherry"] = "sakurambo"
    print(dct)
    print(dct["apple"])
    del dct["cherry"]
    print(dct)
    print("apple" in dct)
    print("cherry" in dct)
    for i in dct:
        print(i)
    print(dct["cherry"])
    