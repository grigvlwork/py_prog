n = int(input())
d = dict()
for i in range(n):
    line = input()
    poster = line[:line.find(' ')]
    views = int(line[line.find(":") + 1:])
    if line.find('опубликовал') != -1:
        row = ['#---#', views]
        d[poster] = row
    else:
        prev_poster = line[line.find('пост у ') + 7:line.find(', ')]
        row = [prev_poster, views]
        d[poster] = row
        next_poster = prev_poster
        while next_poster != '#---#':
            d[next_poster][1] += views
            next_poster = d[next_poster][0]
for val in d.values():
    print(val[1])
