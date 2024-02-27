
# 2.18. Write a program to swap the values of two variables using temporary variable

x = int(input("enter an int variable: "))
y = int(input("enter another int variable: "))

# before swap
print("Before swap")
print("X: ", x)
print("Y: ", y)

# just for new line after it
print()


# swaping values
temp = x # assigning x to temp
x = y # assigning y to x
y = temp # assigning temp to y

# after swap
print("After swap")
print("X: ", x)
print("Y: ", y)

