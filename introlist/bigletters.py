a = [" * ", "* *", "***", "* *", "* *"]
b = ["** ", "* *", "** ", "* *", "** "]
c = [" * ", "* *", "*  ", "* *", " * "]
line = input()
big = ["", "", "", "", ""]
for i in range(5):
    for j in range(len(line)):
        if line[j] == "A":
            big[i] += a[i] + "  "
        elif line[j] == "B":
            big[i] += b[i] + "  "
        else:
            big[i] += c[i] + "  "
    big[i] = big[i][:-2]
    print(big[i])
