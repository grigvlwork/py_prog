def swap(first, second):
    temp = list()
    for line in first:
        temp.append(line)
    first.clear()
    for line in second:
        first.append(line)
    second.clear()
    for line in temp:
        second.append(line)
