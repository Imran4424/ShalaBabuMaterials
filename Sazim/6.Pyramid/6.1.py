# 6.1.    
#		1
#		1 2
#		1 2 3
#		1 2 3 4
#		1 2 3 4 5

# You will learn nested loop deeply doing these pyramids


n = int(input("enter the value of n: "))

# row
for i in range(1, n + 1):
    # col
    for j in range(1, i + 1):
        # value
        print(j, end = " ")
    print()

