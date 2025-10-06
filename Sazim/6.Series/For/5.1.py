# 5.1. Write a program to calculate the series: 1 + 2 + 3 + 4 + ... + n

n = int(input("enter the value of n: "))

sum = 0

for num in range(1, n + 1):
	sum = sum + num


print("series sum is: ", sum)