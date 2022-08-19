###theory
##1.  False
##    True
##    False
##    True
##    True
##    True
##2.  No Flag
##3. There is some fruit
##4.  H
##    B
##    A
##    NO
##    YES
##5.  JANE


#Part II. Programming

###Program1 Temperature with a menu
##
##print("This program converts temperature values.")
##print("")
##print("If you want to convert a temperature from Celsius to Fahrenheiht, enter F.")
##print("If you want to convert a temperature from Fahrenheit to Celsius, enter C.")
##print("")
##option=input("Enter your choice: ")
##print("")
##if option=="F":
##    C= float(input("Enter a temperature in Celcius: "))
##    F= (9/5)*C+32
##    print(format(C,".1f"),"C =",format(F,".2f"),"F")
##elif option=="C":
##    F= float(input("Enter a temperature in Fahrenheit: "))
##    C= (5*(F-32))/9
##    print(format(F,".1f"),"F =",format(C,".2f"),"C")
##else:
##    print("Sorry, there is no such choice in the menu.")




###Program2 Flag variables
##
##print("This program determines if the value is within the right range")
##print("")
##user=float(input("Enter a number: "))
##alert=False
##
##if user>=90 and user<=120:
##    alert=True
##
##if alert:
##    print("The value is OK")
##else:
##    print("The value is risky")




#Program3 SSN Form
#Hyungeeu Choi
print("This program displays nine digit number to SSN format.")

number=input("Enter nine digit number: ")

if len(number)==9:
    SSN=number[:3]+"-"+number[3:5]+"-"+number[5:]
    print("SSN: ",SSN)
else:
    print("You have NOT entered nine digit number")
