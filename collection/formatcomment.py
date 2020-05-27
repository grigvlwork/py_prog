from sys import stdin

lines = list(enumerate([line.rstrip('\n') for line in stdin]))
print('\n'.join(['Line ' + str(k[0] + 1) + ': ' +
                 k[1].lstrip(' #').rstrip(' \t')
                 for k in lines if k[1].lstrip()[0] == '#']))
