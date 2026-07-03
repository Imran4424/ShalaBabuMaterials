# 5.1. Write a program to calculate the series: 1 + 2 + 3 + 4 + ... + n

n = int(input("enter the value n: "))
num = 1
sum = 0

while num <= n:
    sum = sum + num
    num = num + 1

print("Sum of the series", sum)

# python loops
# while loop
# for loop

# 0 - False
# All other number - True