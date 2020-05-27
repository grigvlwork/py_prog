a = float(input())
b = float(input())
op = input()
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print(888888)
else:
    print(888888)
