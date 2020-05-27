heap = int(input())
while heap > 0:
    take = int(input())
    while (take > 3) or (take < 1) or (take > heap):
        print(heap)
        take = int(input())
    heap -= take
    print(heap)
