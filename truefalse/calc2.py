def fact(n):
    p = 1
    for i in range(2, n + 1):
        p *= i
    return p


while True:
    num1 = int(input())
    comm = input()
    if comm == "+":
        print(num1 + int(input()))
    elif comm == "-":
        print(num1 - int(input()))
    elif comm == "*":
        print(num1 * int(input()))
    elif comm == "/":
        num2 = int(input())
        if num2 != 0:
            print(num1 // num2)
    elif comm == "%":
        num2 = int(input())
        if num2 != 0:
            print(num1 % num2)
    elif comm == "!":
        if num1 >= 0:
            print(fact(num1))
    elif comm == "x":
        print(num1)
        break
