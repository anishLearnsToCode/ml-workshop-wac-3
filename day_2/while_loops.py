"""
While Loop

while condition:
    code
    code

condition --> code --> condition --> code --> condition --> code --> condition --> exit loop
"""

isHallFullyBooked = True

# infinite loop
# while False:
#     print('the hall is fully booked')

i = 0
while i >= 0:
    print(i)
    i = i + 1       # i <-- i + 1

# unreachable code
print('i am outside the loop')
print(i + 10)

"""
i = 4
0
1
2
3
4
"""
