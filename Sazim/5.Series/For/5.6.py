
# 5.6. Write a program to calculate the series: 1.2 + 2.3 + 3.4 + ... + n(n+1)

n = int(input("enter the value of n: "))

sum = 0

for num in range(1, n + 1):
	sum = sum + num * (num + 1)

print("series sum is: ", sum)