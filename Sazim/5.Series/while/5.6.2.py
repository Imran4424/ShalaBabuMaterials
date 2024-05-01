# 5.6. Write a program to calculate the series: 1.2 + 2.3 + 3.4 + ... + n(n+1)

n = int(input("enter the value n: "))

num = 1
sum = 0

while num <= n:
    sum = sum + num * (num + 1)
    num = num + 1

print("Sum of the series", sum)