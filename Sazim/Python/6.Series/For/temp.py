
# 5.1. Write a program to calculate the series: 1 + 2 + 3 + 4 + ... + n

n = int(input("enter the value of n: "))

startValue = 1
sum = 0

for num in range(startValue, n + 1):
    sum = sum + num


print("Series sum is ", sum)