subsid = int(input())
amount = int(input())
subsid -= 20
for bull in range(subsid // 20 + 1):
    remain = subsid - bull * 20
    if remain == 0 and amount == bull + 1:
        print(bull + 1, 0, 0)
    else:
        for cow in range((subsid - bull * 20) // 10 + 1):
            remain = subsid - bull * 20 - cow * 10
            if remain == 0 and amount == bull + 1 + cow:
                print(bull + 1, cow, 0)
            else:
                calf = remain // 5
                remain -= calf * 5
                if remain == 0 and amount == bull + 1 + cow + calf:
                    print(bull + 1, cow, calf)
