ways = int(input())
way = -1
height_max = -1
for i in range(ways):
    tunnels = int(input())
    height_min = 10000000
    for j in range(tunnels):
        height_min = min(height_min, int(input()))
    if height_max < height_min:
        height_max = height_min
        way = i + 1
print(way, height_max)
