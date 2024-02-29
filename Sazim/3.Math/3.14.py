
# 3.14. Write a program that read two numbers base, power and display the value of base^power

base = float(input("enter the base: "))
power = float(input("enter the power: "))

# using pow method
result = pow(base, power)

print("Result is ", "{:.4f}".format(result))

# (**) - power operator
anotherResult = base ** power

print("Another result is: ", "{:.4f}".format(anotherResult))