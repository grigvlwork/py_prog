price0 = int(input())
price1 = int(input())
buy = -1
sell = -1
while price1 != 0:
    if price1 > price0 and buy < 0:
        buy = price1
    if price1 < price0 and buy > -1 and sell < 0:
        sell = price1
    price0 = price1
    price1 = int(input())
print(buy, sell, sell - buy)