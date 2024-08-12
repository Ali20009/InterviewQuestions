class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.q = [0] * k
        self.count = 0
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.size:
            return False
        self.q[self.rear] = value
        self.rear = (self.rear+1) % self.size
        self.count += 1

        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.q[self.front] = 0
        self.front = (self.front+1) % self.size
        self.count -= 1
        return  True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.q[self.front]
         

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.q[self.rear-1]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.size == self.count
    
    
a = MyCircularQueue(3)
a.enQueue(1)

a.enQueue(2)
a.enQueue(3)
#print(a.Front())
print(a.Rear())
a.deQueue()
a.enQueue(4)
print(a.Rear())


'''
MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. '''