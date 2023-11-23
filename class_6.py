"""
list1 = [x for x in range(5)]

sqr = lambda x: x ** 2

squared_nums = map(sqr, list1)

print((squared_nums))
#======================================

list1 = [x for x in range(10)]
is_even = lambda x: x % 2 == 0

even_nums_list = list(filter(is_even, list1))
print(even_nums_list)

#======================================

import random

random.seed(42)
value = random.randint(1, 100)
print(value)

rand = random.randint(2, 12)
print(rand)
#======================================

import errno

try:
    file = open("file.txt", "r+")
    print(file.read())

    file.close()
except Exception as e:
    if e.errno == errno.ENOENT:
        print("No such file")
    elif e.errno == errno.EMFILE:
        print("Too many files opened")
#=======================================

ba = bytearray(b"Hello")
ba[0] = 65
print(ba)
#=======================================

import math_operations as m
import math

print(m.add(1, 2))
print(m.subs(1, 2))
print(m.mult(1, 2))
print(m.divide(1, 2))

print(math.pi)
"""
#======================================

import requests
import json

url = "https://canvas.elte.hu/belepes/"
response = requests.get(url)

if response.status_code == 200:
    try:
        data = response.json()
        print(data)
    except json.JSONDecodeError as e:
        print("Error parsing JSON: ", e)
else:
    print("Error: " + str(response.status_code))