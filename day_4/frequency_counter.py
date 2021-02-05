"""
this is amazing course this is so good i am enjoying this course

{
    'this': 3,
    'is': 4,
    'amazing': 1
    ...
    ...
}
key: str (word)
value: int (freq)
"""
from typing import List, Dict

passage: str = input()
frequency: Dict[str, int] = {}
words: List[str] = passage.split()

for word in words:
    frequency[word] = frequency.get(word, 0) + 1


print(frequency)


"""
passage = hello world
frequency = {}
words = ['hello', 'world']
word = 'hello'
freq['hello'] = freq.get('hello') + 1
"""
