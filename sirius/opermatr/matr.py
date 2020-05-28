n = int(input())
a = [[int(i < j and i < (n - j - 1)) +
      2 * int(i < j and i > (n - j - 1)) +
      3 * int(i > j and i > (n - j - 1)) + 
      4 * int(i > j and i < (n - j - 1))
      for j in range(n)] for i in range(n)]
for row in a:
    print(*row) 