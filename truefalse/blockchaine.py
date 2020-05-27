n = int(input())
h0 = 0
num_wrong = -1
for i in range(n):
    block = int(input())
    h = block % 256
    block = block // 256
    r = block % 256
    m = block // 256
    if (h != 37 * (m + r + h0) % 256 or h >= 100) and num_wrong == -1:
        num_wrong = i
    h0 = h
print(num_wrong)
