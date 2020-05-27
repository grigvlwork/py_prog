from datetime import datetime

d1 = datetime.strptime("01.09.2019", "%d.%m.%Y")
d2 = datetime.fromordinal(d1.toordinal() + int(input()))
print(d2.day, d2.month)
