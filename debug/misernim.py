heap = int(input())
while heap > 0:
    if heap == 1:
        take_comp = 1
    elif heap < 5:
        take_comp = heap - 1
    elif heap % 4 < 3:
        take_comp = heap % 4 + 1
    else:
        take_comp = 1
    heap -= take_comp
    print(take_comp, heap)
    if heap > 0:
        take_user = int(input())
        while (take_user > 3) or (take_user < 1) or (take_user > heap):
            print(heap)
            take_user = int(input())
        heap -= take_user
        print(take_user, heap)
