from sys import stdin

print(sum([1 if x.strip()[0] == '#' else 0
           for x in stdin if len(x.strip()) > 0]))
