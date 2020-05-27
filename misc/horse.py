x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
delta1=max(abs(x2-x1),abs(y2-y1))
delta2=min(abs(x2-x1),abs(y2-y1))
if delta1==2 and delta2==1:
	print("YES")
else:
	print("NO")