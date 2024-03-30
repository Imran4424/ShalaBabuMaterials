
# 4.14. Write a program to generate a simple arithmetic calculator

# hints: 
# enter two numbers: 6 5
# select the menu:
# 1. Add
# 2. Substract
# 3. Multiply
# 4. Divide

x = float(input("enter the first number: "))
y = float(input("enter the second number: "))

print("Choose what you want to do.")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

command = int(input("selected operation? "))

result = None

if command == 1:
    result = x + y
elif command == 2:
    result = x - y
elif command == 3:
    result = x * y
elif command == 4:
    if y == 0:
        print("\nError! Can't divide by zero")
    else:
        result = x / y
elif command == 5:
    if y == 0:
        print("\nError! Can't divide by zero")
    else:
        result = x % y
else:
    print("\nError! I will hack your account")
    

print("\nResult is:", result)