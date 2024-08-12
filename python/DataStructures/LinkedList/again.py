class Node:
    def __init__(self, value, next= None) -> None:
        self.value = value
        self.next = next
    
class Linked_List:
    def __init__(self):
        self.head = None

    def insert_first(self, value):
        node = Node(value, self.head)
        self.head = node
         
    def print(self):
        res = ''
        itr = self.head
        while itr:
            res += str(itr.value) + '->' 
            itr = itr.next
        print(res)
    
a = Linked_List()
a.insert_first(4)
a.insert_first(2)
a.insert_first(5)

a.print()

