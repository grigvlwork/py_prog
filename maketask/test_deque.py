from collections import deque
import uuid

a = [[1, 2, 2],
     [2, 3, 4],
     [3, 4, 5]
     ]
b = deque(a)
print(b.pop())
print(str(uuid.uuid4()))


