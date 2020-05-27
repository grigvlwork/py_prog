def pyram(line):
    line_i = [int(s) for s in line.split()]
    pyr = list()
    while len(line_i) > 0:
        if len(line_i) == 1:
            if len(pyr) > 0:
                if line_i[0] <= pyr[-1]:
                    pyr.append(line_i.pop())
                    return pyr
                else:
                    pyr = list()
                    return pyr
            else:
                return line_i
        else:
            if line_i[0] == line_i[-1]:
                p = line_i.pop(0)
                p = line_i.pop()
                if len(pyr) > 0:
                    if p <= pyr[-1]:
                        pyr.append(p)
                        pyr.append(p)
                    else:
                        pyr = list()
                        return pyr
                else:
                    pyr.append(p)
                    pyr.append(p)
            elif line_i[0] > line_i[-1]:
                p = line_i.pop(0)
                if len(pyr) > 0:
                    if p <= pyr[-1]:
                        pyr.append(p)
                    else:
                        pyr = list()
                        return pyr
                else:
                    pyr.append(p)
            else:
                p = line_i.pop()
                if len(pyr) > 0:
                    if p <= pyr[-1]:
                        pyr.append(p)
                    else:
                        pyr = list()
                        return pyr
                else:
                    pyr.append(p)


n = int(input())
for i in range(n):
    pr = pyram(input())
    if len(pr) > 0:
        pr = [str(p) for p in pr]
        print(" ".join(pr))
    else:
        print("НЕТ")
