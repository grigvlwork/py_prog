value = 1
addition = 1
print('value =', value)
print('addition =', addition)
value = value + addition
test1 = value
print('value = value + addition ->', value)
value = 1
addition = 1
value += addition
print('value += addition ->', value)
test2 = value
print('Values is equal - ', test1 == test2)


value = list('1')
addition = [value]
print('value =', value)
print('addition =', addition)
value = value + addition
test1 = value
print('value = value + addition ->', value)
value = list('1')
addition = [value]
value += addition
test2 = value
print('value += addition ->', value)
print('Values is equal - ', test1 == test2)