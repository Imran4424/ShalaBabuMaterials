# 5.7. Write a program to calculate the series: 2.1 + 5.3 + 8.5 + ... + n(n - nth)

n = int(input("enter the value n: "))

num = 2
i = 1
sum = 0

while num <= n:
    sum = sum + num * (num - i)
    num = num + 3
    i = i + 1

print("Sum of the series", sum)