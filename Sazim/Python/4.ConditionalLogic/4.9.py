
# 4.9. Write a program that read mark and display result in grade

mark = float(input("enter subject's mark(0 to 100): "))

if mark >= 80:
    print("A+")
elif mark >= 70:
    print("A")
elif mark >= 65:
    print("A-")
elif mark >= 60:
    print("B")
elif mark >= 50:
    print("C")
elif mark >= 40:
    print("D")
elif mark >= 33:
    print("E")
else:
    print("F")