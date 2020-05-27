logins = input().split(",")
badlogins = list()
allowed = "abcdefghijklmnopqrstuvwxyz"
allowed += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
allowed += "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
allowed += "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
allowed += "_0123456789"
for login in logins:
    flag = True
    for i in range(len(login)):
        if allowed.find(login[i]) == -1:
            flag = False
            break
    if not flag:
        badlogins.append(login)
if len(badlogins) > 0:
    badlogins.sort()
    maxlen = max([len(p) for p in badlogins])
    print("\n".join([" " * (maxlen - len(p)) + p for p in badlogins]))
