
# 2.19. Write a program to swap the values of two variables without using temporary variable

x = int(input("enter an int variable: "))
y = int(input("enter another int variable: "))

# before swap
print("Before swap")
print("X: ", x)
print("Y: ", y)

# just for new line after it
print()


# swaping values
x = x + y # assigning sum of x + y to x
y = x - y # if now x holds sum, then y = x - y = old(x + y) - y
x = x - y # since, now y holds previous x, then x = x - y = old(x + y) - old (x)

# after swap
print("After swap")
print("X: ", x)
print("Y: ", y)

