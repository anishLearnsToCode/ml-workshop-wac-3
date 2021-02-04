"""
Functions
def function_name(parameters_1, parameters_2, parameters_3 ...):
    code
    code
    [optional] return answer_1, answer_2 ...
"""
import math
from typing import Union, Tuple


def hello():
    print('i am inside a function')
    print('hello world')
    print('i am leaving, tata bye bye')


def hello_world(name: str) -> str:
    # print(type(name))
    return 'hello ' + name
    # return 'hello ' + 'anish'
    # return 'helloanish'


def addition(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


def multiplication(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b


def full_name(first_name: str, last_name: str, middle_name=None) -> str:
    if not middle_name:
        return first_name + ' ' + last_name
    return first_name + ' ' + middle_name + ' ' + last_name


def algebra(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Tuple[float, float]:
    """"ax^2 + bx + c = 0"""
    D = math.sqrt(b ** 2 - 4 * a * c)
    return (-b + D) / (2 * a), (-b - D) / (2 * a)


# tuple
# print(algebra(1, 3, 2))
print(full_name('anish', 'sachdeva', middle_name=''))
print(full_name(middle_name='sebastian', first_name='johann', last_name='bach'))
print(full_name('johann', middle_name='sebastian', last_name='bach'))

print('text', end='   ***** ')
