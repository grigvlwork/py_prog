# https://openpyxl.readthedocs.io/en/stable/charts/pie.html
# https://tokmakov.msk.ru/blog/item/71

from openpyxl import Workbook
from openpyxl.chart import PieChart
from openpyxl.chart import Reference
from openpyxl.chart.series import DataPoint
from sys import stdin

wb = Workbook()
ws = wb.active
data = []
i = 0
for s in stdin:
    i += 1
    parametr, value = s.split()
    value = int(value)
    data.append([parametr, value])
for row in data:
    ws.append(row)
pie = PieChart()
labels = Reference(ws, min_col=1, min_row=1, max_row=i)
data = Reference(ws, min_col=2, min_row=1, max_row=i)
pie.add_data(data, titles_from_data=True)
pie.set_categories(labels)
ws.add_chart(pie, "C3")
wb.save('res.xlsx')
