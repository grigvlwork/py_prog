def hideout(maps, *args, not_transform=(), **kwargs):
    new_map = maps.copy()
    for t in args:
        row = t[0][0]
        col = t[0][1]
        trans = t[1]
        if col not in not_transform and trans in kwargs:
            new_map[row][col] = kwargs[trans](new_map[row][col])
    return new_map
