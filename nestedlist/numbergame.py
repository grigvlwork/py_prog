from statistics import median


def maria(n):
    return n * 3 - 2


def peter(n):
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    return n + 11


n = int(input())
name = input()
steps = int(input())
nums = list()
i = 0
if name == "Петя":
    while i < steps:
        n = peter(n)
        nums.append(n)
        i += 1
        if i < steps:
            n = maria(n)
            nums.append(n)
        i += 1
else:
    while i < steps:
        n = maria(n)
        nums.append(n)
        i += 1
        if i < steps:
            n = peter(n)
            nums.append(n)
        i += 1
print(median(nums))
