import random
import math
import os

os.system('cls')

main = int(input("Enter a number: "))
deloc = int(random.randint(0,255))

print(main + deloc)
print('RandInt: ' + str(deloc))
print('Added ' + str(main) + 'which gives us' + main + deloc )