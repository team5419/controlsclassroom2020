import math

alphabet = 'abcdefghijklmnopqrstuvwxyz'
breakpointCheck = 1
returning = ''
def convert(value):
    if(value < 10):
        return value
    else:
        return alphabet[value - 10]

numInTen = int(input('What number would you like to translate? '))
base = int(input('What base should this be in (2 to 36)? '))
if(base < 2 or base > 36):
    print('Not a valid base.')
else: 
    while breakpointCheck * base <= numInTen:
        breakpointCheck *= base

    while breakpointCheck >= 1:
        returning += str(convert(math.floor(numInTen / breakpointCheck)))
        numInTen -= math.floor(numInTen / breakpointCheck) * breakpointCheck
        breakpointCheck /= base

    print('Your number is ' + returning + '!')