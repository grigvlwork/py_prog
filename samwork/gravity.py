n = int(input())
question = input()
if ('не люб' in question and n % 2 == 0) or ('очень люб' in question and n % 2 == 1):
    print('любит')
else:
    print('не любит')
