def find_mountain(heightsMap):
    maxh = heightsMap[0][0]
    maxi = 0
    maxj = 0
    for i in range(len(heightsMap)):
        for j in range(len(heightsMap[i])):
            if heightsMap[i][j] > maxh:
                maxh = heightsMap[i][j]
                maxi = i
                maxj = j
    result = tuple()
    result = (maxi, maxj)
    return result

