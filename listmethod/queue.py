queue = list()
n = int(input())
for i in range(n):
    message = input()
    if message[-18:] == " встала в очередь.":
        queue.append(message[:-18])
    elif message[-17:] == " встал в очередь.":
        queue.append(message[:-17])
    elif message[-16:] == " будет за тобой.":
        exclam = message.find("!")
        first = message[8:exclam]
        second = message[exclam + 2: -16]
        queue.insert(queue.index(first) + 1, second)
    else:
        goaway = message[:-34]
        queue.pop(queue.index(goaway))
print("\n".join(queue))

