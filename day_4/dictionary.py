"""
Dictionary / HashMap / Map

index --> value
int   --> anything
unique    not unique

anything --> anything
key     --> value
unique  --> not unique
{}
- mutable
- iterable
"""

words = {
    'hello': 500,
    'i': 756,
    'am': 500,
    'batman': None
}

# print(type(words))
# print(len(words))
# print(words)

# access keys
# print(words['ball'])
print(words.get('joker'))

# print(words)
# update the value for key
# words['hello'] = 78
# print(words)

# add new key
# words['joker'] = 56
# print(words)

# remove key
del words['hello']
print(words)




# check whether key present in dict or not
# print('Hello' in words)
