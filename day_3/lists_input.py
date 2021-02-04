"""
1 2 3 4 5 100
[1, 2, 3, 4, 5, 100]
"""
from typing import List

user_input = input()
numbers: List[str] = user_input.split()

for index in range(len(numbers)):
    numbers[index] = int(numbers[index])

print(numbers)
