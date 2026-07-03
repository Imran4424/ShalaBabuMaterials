
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
x, y = y, x

# after swap
print("After swap")
print("X: ", x)
print("Y: ", y)
