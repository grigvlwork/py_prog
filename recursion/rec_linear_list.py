def rec_linear_sum(some_list):
    if len(some_list) == 0:
        return 0
    elif len(some_list) == 1:
        return some_list[0]
    else:
        total = some_list.pop() + rec_linear_sum(some_list)
        return total

# print(rec_linear_sum([1.0, 2]))
