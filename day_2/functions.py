"""
Functions
def function_name(parameters_1, parameters_2, parameters_3 ...):
    code
    code
    [optional] return answer_1, answer_2 ...
"""
import math


def hello():
    print('i am inside a function')
    print('hello world')
    print('i am leaving, tata bye bye')


def hello_world(name):
    # print(type(name))
    return 'hello ' + name
    # return 'hello ' + 'anish'
    # return 'helloanish'


def addition(a, b):
    return a + b


def multiplication(a, b):
    return a * b


def full_name(first_name, last_name, middle_name=None):
    if middle_name is None:
        return first_name + ' ' + last_name
    return first_name + ' ' + middle_name + ' ' + last_name


def algebra(a, b, c):
    """"ax^2 + bx + c = 0"""
    D = math.sqrt(b ** 2 - 4 * a * c)
    return (-b + D) / (2 * a), (-b - D) / (2 * a), 'hello', 100


# tuple
# print(algebra(1, 3, 2))
# print(full_name(middle_name='sebastian', first_name='johann', last_name='bach'))
# print(full_name('johann', middle_name='sebastian', last_name='bach'))

print('text', end='   ***** ')
