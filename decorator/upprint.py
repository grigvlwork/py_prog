def upper_print(func):
    def wrapper(*args, **kwargs):
        func(*[i.upper() if hasattr(i, 'upper') else i for i in args], **kwargs)
    return wrapper


print = upper_print(print)


