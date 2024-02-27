
# 3.2. Write a program that read any angle t and display sin(t)

import math

degreeAngle = float(input("enter an angle in degrees: "))

sineValue = math.sin(math.radians(degreeAngle))

print("Sine value is: ", sineValue)