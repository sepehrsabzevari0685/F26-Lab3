# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:sepehr sabzevari 
# Date: 10/8/2026
# Purpose: 
# Usage: ./lab3g.py

# Follow the specific instructions given in the README.md file
mylist = []
while len(mylist) < 6:
    num = int(input("Enter a number: "))
    mylist.append(num * 10)
mylist.reverse()
print(mylist)
 
