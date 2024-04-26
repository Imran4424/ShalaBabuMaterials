# 5.2. Write a program to calculate the series: 2 + 4 + 6 + 8 + ... + n

n = int(input("enter the value n: "))
num = 1
sum = 0

while num <= n:
    if num % 2 == 0:
        sum = sum + num
    num = num + 1

print("Sum of the series", sum)