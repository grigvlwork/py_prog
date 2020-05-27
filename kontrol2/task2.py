def power_of_theater(text, divisor_1, divisor_2, *args, **kwargs):
    a = text.split(divisor_1)
    b = list()
    for elem in a:
        b.append(elem.split(divisor_2))
    for arg in  args:
        if arg[2] in kwargs:
            b[arg[0]][arg[1]] = kwargs[arg[2]](b[arg[0]][arg[1]])
    return b

