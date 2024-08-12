class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class linked_list:
    def __init__(self) -> None:
        self.head = None

    def insertfirst(self, daata):
        node = Node(daata, self.head)
        self.head = node

    def append(self, da):
        if self.head == None:
            self.head = Node(da, None)
            return

        new_node = Node(da, None)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def print(self):
        itr  = self.head
        res = ''

        while itr:
            res += str(itr.data) + '->'
            itr = itr.next
        print(res)

    def insert_values(self,values):
        self.head = None
        for i in values:
            self.append(i)

    def get_length(self):
        count = 0
        i = self.head
        while i:
            count += 1
            i = i.next
        return count
    
    def removeat(self, index):
        if index  < 0 or index >= self.get_length():
            raise Exception('This is not a valid index')
        if index == 0:
            self.head = self.head.next
            return 
        count = 0
        itr = self.head
        while itr :
            if count == index-1:
                itr.next = (itr.next).next
                break
            itr = itr.next
            count += 1

        
        #for i in range(index, self.get_length):
    
    def insert(self, index, value):
        if 0 > index or index > self.get_length():
            return Exception('Ibvalid Index')
        if index == 0:
            node = Node(value, self.head)
            self.head = node
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(value, itr.next)
                itr.next = node
                return
            itr = itr.next
            count += 1
        
    def inser_after_value(self, previous_data, data):
        itr = self.head

        while itr:
            if itr.data == previous_data:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
        return Exception('Invalid Value')
    
    def remove_by_value(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if itr.next.data ==value:
                itr.next = itr.next.next
                return
            itr = itr.next
            
        return Exception('Invalid Value')
            

    
a = linked_list()
a.insertfirst(32)
a.insertfirst(33)
a.insertfirst(34)
a.append(2)

#a.insert_values(['re', 'ed', 'ru'])
a.print()
a.removeat(2)
print(a.get_length())
a.insert(0, 8)
a.remove_by_value(33)
a.inser_after_value(34, 9)
a.print()