width = 30
print('.')
for i in range(width):
    returning = '.'
    for j in range(i):
        returning += ' '
    returning += '.'
    print(returning)
for i in range(width + 2):
    returning = ''
    for j in range(i):
        returning += ' '
    returning += '.'
    for j in range(width - i):
       returning += ' '
    if(i != width + 1):
        returning += '.'
    print(returning)
