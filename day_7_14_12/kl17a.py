import pickle
from dataclasses import dataclass
from kl16a import Person

# @dataclass
# class Person:
#     first_name: str
#     last_name: str
#     id: int
#
#     def greet(self):
#         print(self.first_name)

with open("dane.pickle", "rb") as file:
    p = pickle.load(file)

print(p)
print(type(p))

for person in p:
    person.greet()
# <class 'list'>
# Jan
# Maciej
