n = int(input())

print('@' * n)
k = 0
for i in range(n - 2):
    message = [' ' for _ in range(n)]
    message[0] = message[-1] = '@'
    message[k + 1] = '@'
    message[n - 2 - k] = '@'
    print(''.join(message))
    k += 1
    k = k % (n // 2)
print('@' * n)
