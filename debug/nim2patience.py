heap = [int(input()) for _ in range(2)]
while heap[0] + heap[1] > 0:
    h = int(input()) - 1
    s = int(input())
    heap[h] -= s
    print(heap[0], heap[1])










