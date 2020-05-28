def get_count(prev_level, n):
    if 0 == n:
        return 1
    count = 0
    for level in range(1, prev_level):
        if n - level < 0: 
            break
        count += get_count(level, n - level)
    return count

n = int(input())
print(get_count(n+1, n))
