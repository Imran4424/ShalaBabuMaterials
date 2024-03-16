
# 4.7. Write a program that read three numbers and display median

x = float(input("enter the first number: "))
y = float(input("enter the second number: "))
z = float(input("enter the third number: "))


# finding middle value among three

if (x > y and x < z) or (x > z and x < y):
    print("median is: ", x)
elif (y > z and y < x) or (y > x and y < z):
    print("median is: ", y)
elif (z > y and z < x) or (z > x and z < y):
    print("median is: ", z)