def left(dir):
    if dir == "север":
        new_dir = "запад"
    elif dir == "запад":
        new_dir = "юг"
    elif dir == "юг":
        new_dir = "восток"
    elif dir == "восток":
        new_dir = "север"
    return new_dir


def right(dir):
    if dir == "север":
        new_dir = "восток"
    elif dir == "запад":
        new_dir = "север"
    elif dir == "юг":
        new_dir = "запад"
    elif dir == "восток":
        new_dir = "юг"
    return new_dir


x_t = int(input())
y_t = int(input())
direction = "север"
new_direction = "север"
x = 0
y = 0
if x == x_t and y == y_t:
    print(0)
    print("север")
    exit(0)
dx = 0
dy = 1
command = input()
flag = False
directive = 1
while command != "стоп":
    if not flag:
        if command == "вперёд":
            step = int(input())
            x += dx * step
            y += dy * step
            if x == x_t and y == y_t:
                flag = True
        elif command == "налево":
            new_direction = left(direction)
        elif command == "направо":
            new_direction = right(direction)
        elif command == "разворот":
            new_direction = left(left(direction))
        if new_direction != direction:
            direction = new_direction
            if direction == "север":
                dx = 0
                dy = 1
            elif direction == "юг":
                dx = 0
                dy = -1
            elif direction == "восток":
                dx = 1
                dy = 0
            elif direction == "запад":
                dx = -1
                dy = 0
    else:
        if command == "вперёд":
            step = int(input())
    try:
        command = input()
        if not flag:
            directive += 1
    except (ValueError, EOFError):
        break
print(directive)
print(direction)
