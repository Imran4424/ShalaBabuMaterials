
# 2.15. Write a program that read a number and multiply by five using shift operator

x = int(input("enter an int number: "))

multiplyByFive = (x << 2) + x

print("Result after multiply by 2: ", multiplyByFive)