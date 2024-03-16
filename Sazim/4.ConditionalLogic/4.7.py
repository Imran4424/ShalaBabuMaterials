
# 4.7. Write a program that read three numbers and display median

x = float(input("enter the first number: "))
y = float(input("enter the second number: "))
z = float(input("enter the third number: "))


# finding middle value among three

# considering x = 8, y = 4, z = 5
# for comments

if x > y and x < z: # 1 and 0 -> 0
    print("median is: ", x)
elif x > z and x < y:
    print("median is: ", x)
elif y > z and y < x: # 0 and 1 -> 0
    print("median is: ", y)
elif y > x and y < z:
    print("median is: ", y)
elif z > x and z < y: # 0 and 0 -> 0
    print("median is:", z)
elif z > y and z < x: # 1 and 1 -> 1
    print("median is:", z)
    

# Binary operators
# Logical operators
# and - logical and
# or - logical or
# not - logical not