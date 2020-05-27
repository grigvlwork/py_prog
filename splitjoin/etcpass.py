st = input()
etc = list()
while st:
    line = st.split(":")
    etc.append([line[0], line[1], line[4].split(",")[0]])
    st = input()
simple = input().split(";")
for empl in etc:
    if empl[1] in simple:
        print("To: " + empl[0])
        print(empl[2] + ", ваш пароль слишком простой, смените его.")
