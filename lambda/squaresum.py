print(sum(list(map(lambda x: x * x, list(filter(lambda x: x % 9 == 0, list(range(18, 100))))))))
