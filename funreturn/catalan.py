cats = dict()
cats[0] = 1


def catalan(n):
    if n == 0:
        return 1
    cat = 0
    for i in range(n):
        if i not in cats.keys():
            cats[i] = catalan(i)
        if n - i - 1 not in cats.keys():
            cats[n - i - 1] = catalan(n - i - 1)
        cat += cats[i] * cats[n - i - 1]
    return cat
