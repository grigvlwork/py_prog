n = int(input())
recipe = list()
for i in range(n):
    s = input()
    if s.find("лук") == -1:
        recipe.append(s)
print(", ".join(recipe))

