message = input()
for i in range(len(message) - 1):
    print(ord(message[i]), end=", ")
print(ord(message[-1]))