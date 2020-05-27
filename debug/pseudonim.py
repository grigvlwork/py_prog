heap = int(input())
while heap > 0:
    take_comp = heap % 4
    heap -= take_comp
    print(take_comp, heap)
    if heap > 0:
        take_user = int(input())
        while (take_user > 3) or (take_user < 1) or (take_user > heap):
            print(heap)
            take_user = int(input())
        heap -= take_user
        print(take_user, heap)
