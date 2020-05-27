queue = list()
n = int(input())
for i in range(n):
    message = input()
    if message[:3] == "Кто":
        queue.append(message.split(" - ")[1][:-1])
    elif message[:3] == "Я т":
        queue.insert(0, message.split(" - ")[1][:-1])
    else:
        if len(queue) > 0:
            print("Заходит " + queue.pop(0) + "!")
        else:
            print("В очереди никого нет.")
