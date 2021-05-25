from collections import deque
from random import choice

a = [[1, 2, 2],
     [2, 3, 4],
     [3, 4, 5]
     ]
b = deque(a)
print(b.pop())
print(eval("choice(list(range(500)))"))


