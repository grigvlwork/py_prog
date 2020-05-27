from openpyxl import Workbook
from sys import stdin

wb = Workbook()
ws = wb.active
data = []
i = 0
for s in stdin:
    i += 1
    product, price, amount = s.split()
    formula = '=B' + str(i) + '+C' + str(i)
    data.append([product, price, amount, formula])
data.append('Итого:','', '', '=СУММ(D1:D' + str(i) + ')')
for row in data:
    ws.append(row)
wb.save('res.xlsx')
