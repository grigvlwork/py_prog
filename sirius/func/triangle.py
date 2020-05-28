def triange(a, b, c):
    return a + b > c and a + c > b and b + c > a

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if triange(a, b, c) or triange(a, b, d) or triange(a, c, d) or \
   triange(b, c, d):
    print('YES')
else:
    print('NO')