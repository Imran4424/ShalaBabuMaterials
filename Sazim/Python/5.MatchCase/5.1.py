# 5.1. Write a program that read a digit and diplay by spelling

number = int(input("enter an int number: "))

match number:
	case 0:
		print("Zero")
	case 1:
		print("One")
	case 2:
		print("Two")
	case 3:
		print("Three")
	case 4:
		print("Four")
	case 5:
		print("Five")
	case 6:
		print("Six")
	case 7:
		print("Seven")
	case 8:
		print("Eight")
	case 9:
		print("Nine")
	case _:
		print("Not a digit")

