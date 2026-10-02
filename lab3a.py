# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: sepehr sabzevari
# Date: 10/2/2026
# Purpose: 
# Usage: ./lab3a.py


import random

numbers = []

for i in range(20):
  num=random.randint(0,99)
  numbers.append(num)
  
print(numbers)
numbers.sort()
print(numbers)
