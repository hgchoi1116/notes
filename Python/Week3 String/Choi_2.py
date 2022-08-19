#Hyungeeu Choi
#Homework2 for week 3

#Problem: Circle menu

import math
print("This program displays the circumference and/or the area of a circle based on user's choice.")
print("")

#input
radius=float(input("Enter the radius of the circle: "))

#calculation
C=2*math.pi*radius
A=math.pi*radius**2

#output
print("")
print("For CIRCUMFERENCE, \tenter C.")
print("For AREA, \t\tenter A.")
print("For BOTH, \t\tenter B.")
print("")
choice=input("Enter your choice: ")
print("")
if choice=="C" or choice=="c":
    print("Circumference: ",format(C,".2f"))
elif choice=="A" or choice=="a":
    print("Area: ",format(A,".2f"))
elif choice=="B" or choice=="b":
    print("Circumference: \t",format(C,".2f"))
    print("Area: \t\t",format(A,".2f"))
else:
    print("There is no such choice in the menu.")


