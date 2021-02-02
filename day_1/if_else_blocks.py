"""
if condition1:
    code1
elif condition2:
    code2
elif condition3:
    code3
..
..
..
..
..
"""

number = int(input())

# indentation
if number == 0:
    print('puny number')
elif number < 10:
    print('small number')
elif number == 10:
    print('this number is the perfect number')
    print('well done :)')
elif number < 100:
    print('mehhh')
else:
    print('default case')
    print('very large number')

print('i am outside the if else block')
