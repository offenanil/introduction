import math

# help(math)
from typing import List, Any

value = 4.35
print(math.floor(value))  # 4

print(math.ceil(value))  # 5

print(round(4.35))  # 4
print(round(4.68))  # 5

from math import pi

print(pi)
print(math.e)
print(math.inf)
print(math.nan)
print(math.log(math.e))
print(math.log(100, 10))

print(math.sin(10))
print(math.degrees(pi / 2))
print(math.radians(180))



# now for the random numbers

# pseudorandom numbers generators

import random

print(random.randint(0, 100))  # choose any random numbers between 0 to 100

random.seed(101)
print(random.randint(0, 100))  # output will be same over and over execution on that cell but output will be different in different cell(no changing value)

print(random.randint(0, 100))

mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))

# sample with replacement
print(random.choices(population=mylist,k=10))      #k is the how many items you want

# sample without replacement
print(random.sample(population=mylist,k=10))   # no numbers are repeated

random.shuffle(mylist)

print(random.uniform(a = 0, b = 100))  #any number between 0 to 100 in floating point value

# look numpy library


