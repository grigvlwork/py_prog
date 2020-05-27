shift = int(input())
message = input()
coded = ""
for i in range(len(message)):
    if ord("А") <= ord(message[i]) <= ord("Я"):
        if ord(message[i]) + shift <= ord("Я"):
            coded += chr(ord(message[i]) + shift)
        else:
            coded += chr(ord("А") + ord(message[i]) + shift - ord("Я") - 1)
    elif ord("а") <= ord(message[i]) <= ord("я"):
        if ord(message[i]) + shift <= ord("я"):
            coded += chr(ord(message[i]) + shift)
        else:
            coded += chr(ord("а") + ord(message[i]) + shift - ord("я") - 1)
    else:
        coded += message[i]
print(coded)
