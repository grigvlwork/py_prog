n = int(input())
text = list()
for i in range(n):
    text.append(input())
n = int(input())
query = list()
for i in range(n):
    query.append(input())
for st in text:
    flag = True
    for qry in query:
        if st.find(qry) == -1:
            flag = False
            break
    if flag:
        print(st)
