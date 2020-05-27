def recursive_reverse(some_list):
    block = list()
    if len(some_list) > 0:
        block.append(some_list.pop())
        block.extend(recursive_reverse(some_list))
    return block

# print(*recursive_reverse([1, 2, 3]))
