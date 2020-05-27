def linear(some_list):
    if len(some_list) == 0:
        return []
    elif len(some_list) == 1:
        if isinstance(some_list[0], list):
            return linear(some_list[0])
        else:
            return some_list
    else:
        if isinstance(some_list[0], list):
            return linear(some_list[0]) + linear(some_list[1:])
        else:
            return [some_list[0]] + linear(some_list[1:])

# print(*linear([[1, 2], 4, [[2, 4, 8, [-4, "er", [0], [{2: "primer"}], []]]]]))
