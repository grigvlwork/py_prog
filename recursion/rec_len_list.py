def recursive_len(some_list):
    if len(some_list) == 0:
        return 0
    else:
        k = 0
        some_list.pop()
        k = 1 + recursive_len(some_list)
        return k

# print(recursive_len([1, 2, 3]))
