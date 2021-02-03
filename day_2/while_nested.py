i = 1
while i < 10:
    j = 0

    while j < 3:
        print(i + j, end=' ')
        j += i

    i += j + 1       # i = i + j + 1
    print()

print(i + j)

"""
i = 11
j = 5
1 2 3 
5 
16
"""
