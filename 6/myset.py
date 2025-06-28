from linked_list import Node, LinkedList
from mydict import MyDict, DictTuple

# class MySet(LinkedList):
#     def __str__(self) -> str:
#         result = "{"

#         node = self.head
#         while node is not None:
#             result += str(node)
#             if node.next is not None:
#                 result += ", "
#             node = node.next

#         result += "}"
#         return result
    
#     def add(self, value):
#         if value in self:
#             return
#         self.push_front(value)
    
#     def remove(self, value):
#         node = self.head
#         prev = None
#         while node is not None:
#             if node.value == value:
#                 if prev is None:
#                     self.head = node.next
#                 else:
#                     prev.next = node.next
#                 return
#             prev = node
#             node = node.next

class MySet(MyDict):
    def __str__(self) -> str:
        result = "{"

        node = self.head
        while node is not None:
            result += str(node.value.key)
            if node.next is not None:
                result += ", "
            node = node.next

        result += "}"
        return result
    
    def add(self, value):
        if value in self:
            return
        self[value] = None
    
    def remove(self, value):
        del self[value]

if __name__ == "__main__":
    st = MySet()
    st.add(1)
    st.add(1)
    st.add(2)
    st.add(3)
    print(st)
    st.remove(3)
    print(st)
    st.remove(1)
    print(st)
    st.remove(1)