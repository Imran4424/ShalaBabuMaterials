
# 2.8. Write a program that read temperature in Celsius and display in Farenheit

celsius = float(input("enter the temperature in celcius: "))

# c / 5 = (f - 32) / 9
# (c * 9) / 5 = f - 32
# ((c * 9) / 5) + 32 = f
# f = ((c * 9) / 5) + 32
farenheit = ((celsius * 9) / 5) + 32

print("Temperature in farenheit is: ", farenheit)