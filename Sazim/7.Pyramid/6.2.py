# 6.2.    
#		1
#		2 2
#		3 3 3
#		4 4 4 4
#		5 5 5 5 5

n = int(input("enter the value of n: "))

# row
for i in range(1, n + 1):
    # col
    for j in range(1, i + 1):
        # value
        print(i, end = " ")
    print()