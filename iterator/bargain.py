import sys

lines = []
for i in range(4):
    lines.append(input())
# lines = [line for line in sys.stdin]
books = lines[0].split('\t')[1:]
min_price_index = 1
for i in range(1, len(lines)):
    if sum([int(k) for k in lines[i].split('\t')[1:]]) < \
            sum([int(k) for k in lines[min_price_index].split('\t')[1:]]):
        min_price_index = i
prices = [int(k) for k in lines[min_price_index].split('\t')[1:]]
market = lines[min_price_index].split('\t')[0]
print(market)
for i in zip(books, prices):
    print(i[0] + '\t' + str(i[1]))
