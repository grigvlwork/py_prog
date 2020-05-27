a = input().split()
a_even = a[::2]
a_odd = a[1::2][::-1]
t = []
for i in range(len(a_odd)):
    t.append(a_even[i])
    t.append(a_odd[i])
if len(a) % 2 == 1:
    t.append(a[-1])
print(*t)
