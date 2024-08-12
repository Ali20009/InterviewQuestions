class ListNode:
    def __init__(self, key= -1, value =-1, next= None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]  # because the first one is dummyNode
        while cur.next:
            if cur.next.key == key:
                cur.next.vlaue = 5
                return
            cur = cur.next
        cur.next = ListNode(key, value)     

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def hash(self, key):
        return key % 1000

    
dic = MyHashMap()
dic.put(4, 8)
dic.put(4,2)
dic.put(4, 9)
print(dic.get(4))
#finish