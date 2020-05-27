sequence = list()
n = int(input())
sequence.append(0)
for i in range(1, n):
    k = 0
    rev_seq = sequence[::-1]
    for j in range(i):
        if rev_seq[j] == sequence[j]:
            k += 1
    sequence.append(k)
for item in sequence:
    print(item)
