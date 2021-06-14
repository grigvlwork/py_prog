from math import pi, sin, cos

f = open('mathtables.py', 'w')
a = dict()
for i in range(361):
    a[i * pi / 180] = [sin(i * pi / 180), cos(i * pi / 180)]
text = "sc_table = " + str(a)
f.write(text)
f.close()
