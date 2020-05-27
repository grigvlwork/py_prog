n = int(input())
text = list()
for i in range(n):
    text.append(input())
query = input()
for st in text:
    if st.find(query) > -1:
        print(st)
