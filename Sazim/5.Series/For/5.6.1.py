
# 5.6. Write a program to calculate the series: 1.2 + 2.3 + 3.4 + ... + n(n+1)

n = int(input("enter the value of n: "))

sum = 0

for i, j in zip(range(1, n + 1), range(2, n + 2)):
	sum = sum + i * j

print("series sum is: ", sum)