heap = [int(input()) for _ in range(3)]
if heap[0] == heap[1]:
    print('Move 1 : AI took', heap[2], 'from heap 3')
    heap[2] = 0
    h1 = 0
    h2 = 1
elif heap[1] == heap[2]:
    print('Move 1 : AI took', heap[0], 'from heap 1')
    heap[0] = 0
    h1 = 1
    h2 = 2
elif heap[0] == heap[2]:
    print('Move 1 : AI took', heap[1], 'from heap 2')
    heap[1] = 0
    h1 = 0
    h2 = 2
else:
    print('Move 1 : AI took', heap[0], 'stones from heap 1')
    heap[0] = 0
    h1 = 1
    h2 = 2
print(heap)
player = 1
move = 1
while heap[h1] + heap[h2] > 0:
    if player == 1:
        h = int(input('heap = ')) - 1
        stones = int(input('stones = '))
        while (heap[h] - stones < 0) or (stones <= 0):
            print('wrong move')
            h = int(input('heap = ')) - 1
            stones = int(input('stones = '))
        heap[h] -= stones
        player = 0
        move += 1
        print('Move', move, ': Human took', stones, 'stones from heap', h + 1)
        print(heap)
    else:
        if heap[h1] != 0 and heap[h2] != 0:
            if heap[h1] > heap[h2]:
                move += 1
                print('Move', move, ': AI took', heap[h1] - heap[h2], 'stones from heap', h1 + 1)
                player = 1
                heap[h1] = heap[h1] - (heap[h1] - heap[h2])
                print(heap)
            elif heap[h1] < heap[h2]:
                move += 1
                print('Move', move, ': AI took', heap[h2] - heap[h1], 'stones from heap', h2 + 1)
                player = 1
                heap[h2] = heap[h2] - (heap[h2] - heap[h1])
                print(heap)
            else:
                move += 1
                print('Move', move, ': AI took 1 stone from heap', h1 + 1)
                player = 1
                heap[h1] -= 1
                print(heap)
        elif heap[h1] == 0:
            move += 1
            print('Move', move, ': AI took', heap[h2], 'stones from heap', h2 + 1)
            player = 1
            heap[h2] = 0
            print(heap)
        elif heap[h2] == 0:
            move += 1
            print('Move', move, ': AI took', heap[h1], 'stones from heap', h1 + 1)
            player = 1
            heap[h1] = 0
            print(heap)
if player == 1:
    print('AI win!')
else:
    print('Human win!')

    








