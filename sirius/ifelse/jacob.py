n = int(input())
m = int(input())
x = int(input())
y = int(input())
if n>m:
    d1 = m-x
    d2 = n-y
else:
    d1 = n-x
    d2 = m-y
if x<d1:
    m1 = x
else:
    m1 = d1
if y<d2:
    m2 = y
else:
    m2 = d2
if m1<m2:
    print(m1)
else:
    print(m2)