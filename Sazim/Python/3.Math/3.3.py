
# 3.3. Write a program that read any angle t and display cos(t)

import math

degreeAngle = float(input("enter an angle in degrees: "))

cosineValue = math.cos(math.radians(degreeAngle))

print("cosine value is: ", "{:.4f}".format(cosineValue))

# taking 4 space floating point float variable as usable variable
cosineValue = "{:.4f}".format(cosineValue)

print("cosine value is: ", cosineValue)