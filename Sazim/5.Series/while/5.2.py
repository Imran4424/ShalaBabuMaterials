# 5.2. Write a program to calculate the series: 2 + 4 + 6 + 8 + ... + n

n = int(input("enter the value n: "))
sum = 0
num = 2

while num <= n:
    sum = sum + num
    num = num + 2
    
print("Sum of the series", sum)