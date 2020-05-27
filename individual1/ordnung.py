n = int(input())
for i in range(n):
    seq1 = [int(k) for k in input().split()]
    f_min = min(seq1)
    f_max = max(seq1)
    print(f_min, f_max)
    print(' '.join([k for k in input().split()
                    if int(k) < (2 * (f_min + f_max) / 3)]))
