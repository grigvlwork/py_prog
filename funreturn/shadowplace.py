def make_shades(alley, k):
    shaded = [False for _ in range(len(alley))]
    for i in range(len(alley)):
        if alley[i] > 0:
            for j in range(alley[i] * abs(k) + 1):
                if k > 0:
                    if i + j in range(len(alley)):
                        shaded[i + j] = True
                else:
                    if i - j in range(len(alley)):
                        shaded[i - j] = True                    
    return shaded


def calculate_sunny_length(shades):
    total = 0
    for meter in shades:
        if not meter:
            total += 1
    return total


def main():
    k = int(input())
    alley = [int(s) for s in input().split()]
    if calculate_sunny_length(make_shades(alley, k)) > 9:
        print('Обгорел')
    else:
        print('Тени достаточно')


def str_to_bool(s):
    if s == 'True':
        return True
    else:
        return False


command = input()
if command == 'main()':
    main()
elif command[:19] == 'print(make_shades([':
    alley = [int(s) for s in command[command.find('[') + 1:command.find(']')].split(',')]
    k = int(command[command.find('],') + 2:command.find('))')])
    print(make_shades(alley, k))
elif command[:30] == 'print(calculate_sunny_length([':
    shades = [str_to_bool(s.strip()) for s in command[command.find('[') +
                                                      1:command.find(']')].split(',')]
    print(calculate_sunny_length(shades))
                
    



