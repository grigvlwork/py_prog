k, a, b = [int(i) for i in input().split()]
print(*set([int(i) for i in input().split()
            if int(i) % k in range(a, b + 1)]))
