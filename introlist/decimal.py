denominator = int(input())
reminder = 1
leng = 0
result = ""
while reminder > 0 and leng < 92001:
    if reminder < denominator:
        reminder *= 10
        result += "0"
    else:
        result += str(reminder // denominator)
        reminder = reminder % denominator * 10
    leng += 1
period = 1
result = result[1:]
if len(result) < 92000:
    print(0)
else:
    for shift in range(500):
        new_result = result[shift:]
        period = 1
        while new_result[:period] != new_result[11 * period: 12 * period] and \
                new_result[:period] != new_result[7 * period: 8 * period] \
                and period < len(new_result) // 2:
            period += 1
        if period < len(new_result) // 2:
            break
    print(new_result[:period])
