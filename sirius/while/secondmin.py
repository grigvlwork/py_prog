prev_min = int(input())
t = int(input())
prev_min, next_min = max(prev_min, t), min(prev_min, t)
t = int(input())
while t != 0:
    if t < next_min:
        prev_min, next_min = next_min, t
    elif t < prev_min:
        prev_min = t 
    t = int(input())
print(prev_min)