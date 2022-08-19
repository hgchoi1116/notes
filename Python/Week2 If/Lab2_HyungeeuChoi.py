#Hyungeeu Choi
#Program #2 Largest
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
