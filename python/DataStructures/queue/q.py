from collections import deque
import queue


q = deque()
q.appendleft(3)
q.appendleft(8)
q.append(7)
print(q.pop())

print (q)
print(dir(q))