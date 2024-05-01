# 5.6. Write a program to calculate the series: 1.2 + 2.3 + 3.4 + ... + n(n+1)

n = int(input("enter the value n: "))

x = 1
y = 2
sum = 0

while x <= n:
    sum = sum + x * y
    x = x + 1
    y = y + 1

print("Sum of the series", sum)