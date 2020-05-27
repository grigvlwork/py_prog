from datetime import datetime


def is_it_possible_to_collect(days):
    dt = datetime.strptime("01.01.2020", '%d.%m.%Y').date()
    dt = datetime.fromordinal(dt.toordinal() + days)
    if dt.weekday() != 4 and dt.weekday() != 6:
        flag = True
    else:
        flag = False
    return dt.strftime('%d.%m.%Y') + " " + str(flag)


print(is_it_possible_to_collect(1))
print(is_it_possible_to_collect(37))
