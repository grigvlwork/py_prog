maxlen = int(input())
n = int(input())
for i in range(n):
    head = input()
    if len(head) > maxlen:
        head = head[:maxlen - 3] + "..."
    print(head)
