spectrum_dict = {'Te': [238.33, 238.58], 'Au': [242.8, 267.6], 'C': [447.86],  
                 'B': [249.68, 249.77], 'Pb': [261.42, 280.2, 283.31, 363.96, 368.35, 405.78],  
                 'Al': [308.22, 309.27, 394.4, 396.15], 'O': [470, 777, 656], 'H': [656.5, 364.7],  
                 'Cs': [455.53, 459.32]}


def atoms(formula):
    global spectrum_dict
    t = dict()
    while len(formula) > 0:
        atom = formula[:1]
        if len(formula) > 1:
            if formula[1].islower():
                atom = formula[:2]
        if atom in spectrum_dict and len(formula) > len(atom):
            if formula[len(atom)].isdigit():
                i = len(atom) + 1
                num = formula[len(atom)]
                while i < len(formula):
                    if formula[i].isdigit():
                        num = num + formula[i]
                    else:
                        break
                    i += 1
                if atom in t:
                    t[atom] += int(num)
                else:
                    t[atom] = int(num)
                if i == len(formula):
                    formula = ''
                else:
                    formula = formula[i:]
            else:
                if atom in t:
                    t[atom] += 1
                else:
                    t[atom] = 1
                formula = formula[len(atom):]
        elif atom in spectrum_dict and len(formula) == len(atom):
            formula = ''
            t[atom] = 1

    return t


substance = dict()
f = open('input.txt', 'r')
for line in f:
    line = line.rstrip('\n')
    for atom, amount in atoms(line).items():
        if atom in substance:
            substance[atom] += amount
        else:
            substance[atom] = amount
sub_list = [[atom, amount] for atom, amount in substance.items()]
sub_list.sort(key=lambda x: (-x[1], x[0]))
for row in sub_list:
    print('Элемент', row[0] + ':', str(row[1]) + ',', sorted(spectrum_dict[row[0]]))
