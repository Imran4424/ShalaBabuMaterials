
# 2.6. Write a program that read two integer and display remainder

x = int(input("enter the first int number: "))
y = int(input("enter the second int number: "))

while y == 0:
    print("second number is zero, we can divide a number with zero")
    y = int(input("enter the second int number: ")) 

print("Remainder is: ", x % y)



# Arithmetic operator
# + : plus - adds two values
# - : minus - substracts second from first number
# * : product or multipication - product of two numbers
# / : divide - give your result when you x / y
# % : modulus - giv you remainder when you x % y