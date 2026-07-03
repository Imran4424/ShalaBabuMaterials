
# 3.15. Write a program that read any number and display it's square root

import math

number = float(input("enter a number: "))

result = math.sqrt(number)

print("Sqaure root is: ", "{:.4f}".format(result))