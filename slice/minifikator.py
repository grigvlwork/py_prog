n = int(input())
for i in range(n):
    st = input()
    pos = 0
    st_min = ""
    while st[pos] == " " and pos < len(st):
        st_min += st[pos]
        pos += 1
    while pos < len(st):
        if st[pos] == "'":
            st_min += st[pos]
            pos += 1
            while pos < len(st):
                if st[pos] != "'" or \
                        (st[pos] == "'" and st[pos - 1] == "\\" and st[pos - 2] != "\\"):
                    st_min += st[pos]
                    pos += 1
                else:
                    st_min += st[pos]
                    pos += 1
                    break
        elif st[pos] == "#":
            break
        elif st[pos] == " ":
            st_min += st[pos]
            pos += 1
            while st[pos] == " " and pos < len(st):
                pos += 1
        else:
            st_min += st[pos]
            pos += 1
    print(st_min)
