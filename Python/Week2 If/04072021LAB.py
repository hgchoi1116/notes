###Theory
###1
##3
##2
##10
##0
##
###2
##20
##
###3
##YY
##ZZ
##WW
##
###4
##DD
##
###5
##CASE A
##The result is excelent
##The result is good
##
##CASE B
##The result is good
##
##CASE C
##The result is excelent


###Program1 BMI
##weight=float(input("Enter your weight(lb): "))
##height=float(input("Enter your height(in): "))
##
##BMI=weight*703/(height**2)
##
##if BMI>25:
##    print("Overweight")
##elif BMI>=18.5 and BMI<=25:
##    print("Optimal")
##else:
##    print("Underweight")


#Hyungeeu Choi
#Program2 Largest
print("This program displays the largest integer.")
number1=int(input("Enter the first integer: "))
number2=int(input("Enter the second integer: "))
number3=int(input("Enter the third integer: "))

if number1>=number2 and number1>=number3:
    print("The largest integer is:",number1)
elif number2>=number1 and number2>=number3:
    print("The largest integer is:", number2)
else:
    print("The largest integer is:",number3)


###Program3 Roulette
##pocket=int(input("Enter a pocket number between 0-36: "))
##
##if pocket==0:
##    print("green")
##elif (pocket>=1 and pocket<=10) or (pocket>=19 and pocket<=28):
##    if pocket%2==0: #even
##        print("black")
##    else:
##        print("red")
##elif (pocket>=11 and pocket<=18) or (pocket>=29 and pocket<=36):
##    if pocket%2==0: #even
##        print("red")
##    else:
##        print("black")
##else:
##    print("There is no color assigned to this number.")
