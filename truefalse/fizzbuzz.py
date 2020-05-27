a = int(input())
b = int(input())
for i in range(a, b + 1):
    ans = ""
    if i % 3 == 0:
        ans = "Fizz"
    if i % 5 == 0:
        ans += "Buzz"
    if ans:
        print(ans)
    else:
        print(i)
