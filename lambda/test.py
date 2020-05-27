def new_print(*args):
    print(' '.join([str(a).upper() for a in args]))
    return True


print = new_print()
print('test')


