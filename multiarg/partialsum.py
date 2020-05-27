def partial_sums(*args):
    ps = [0]
    total = 0
    for arg in args:
        total += arg
        ps.append(total)
    return ps
