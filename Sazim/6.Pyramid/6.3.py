# 6.3.    
#		1
#		0 0
#		1 1 1
#		0 0 0 0
#		1 1 1 1 1

n = int(input("enter the value of n: "))

# row
for r in range(1, n + 1):
    # col
    for c in range(1, r + 1):
        # value
        if r % 2 == 0:
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()
