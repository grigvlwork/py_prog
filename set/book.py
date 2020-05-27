m = int(input())
n = int(input())
book_home = set()
for i in range(m):
    book_home.add(input())
for i in range(n):
    if input() in book_home:
        print("YES")
    else:
        print("NO")
