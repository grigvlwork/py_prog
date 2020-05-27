dv = set('dvorak')
print(len([len(set(s) & dv) for s in input().lower().split('\\')
           if len(set(s) & dv) == 1 or len(set(s) & dv) == 3]))
