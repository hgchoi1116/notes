#04212021 Lab


##print("#1")
##for value in range(-10,-2,2):
##    print(value)
####1.  -10
####    -8
####    -6
####    -4
##
##print("#2")
##for value in range(3,7):
##    if value%2==0:
##        print("AA")
##    else:
##        print("BB")
####2.  BB
####    AA
####    BB
####    AA
##
##print("#3")
##sign="$$"
##for num in [1,3,1,3,1]:
##    print(sign*num)
####3.  $$
####    $$$$$$
####    $$
####    $$$$$$
####    $$
##
##print("#4")
##data=['1','2','3','4',]
##result=""
##for element in data:
##    result+=element*2
##print(result)
####4.  11223344
##
##print("#5")
##data=[15,4,10,15]
##total=0
##for number in data:
##    total+=number
##print(total)
####5.  44
##
##print("#6")
##total=1
##for number in range(1,10,3): #1,4,7
##    total*=number
##    print(total)
####6.  1
####    4
####    28
##
##print("#7")
##for value in range(2,10,3): #2,5,8
##    if value>=5:
##        print("XX")
##    else:
##        print("YY")
####7.  YY
####    XX
####    XX


#Program1
#Sum of squares
print("This program displays a sum of first n squares.")
user_int=int(input("How many squares do you want in the sum?"))
print("")
total=0
for value in range (1,user_int+1):
    total+=value**2
print("1^2+2^2+3^2+...+",user_int,"^2 =",total)


###Program2 lab4.py
###Hyungeeu Choi
##print("This program displays info about the entered positive integer.")
##user_int=int(input("Enter a positive integer: "))
##even=0
##odd=0
##for digit in str(user_int):
##    if int(digit)%2==0:
##        even+=1
##    else:
##        odd+=1
##
##print("There are",even,"even digits.")
##print("There are",odd,"odd digits.")


#Program3
# KG vs LB
print("This is a weight convertor.")
print("INFO: 1 pound (lb) is equal to 0.45359237 kilograms (kg).")
print("")
user_number=int(input("How many conversions do you want to make?"))

CONVERSION=0.45359237

for number in range(1,user_number+1):
    print("")
    print("Conversion #", number)
    print("*** If you want to convert kg to lb, enter 1.***")
    print("*** If you want to convert lb to kg, enter 2.***")
    print("")
    choice=int(input("Enter your choice:"))
    if choice==1:
        user_weight=float(input("Enter a weight in kilograms: "))
        new_weight=user_weight/CONVERSION
        print(format(user_weight,".2f"),"kg =",format(new_weight,".2f"),"lb")
    else:
        user_weight=float(input("Enter a weight in pounds: "))        
        new_weight=user_weight*CONVERSION
        print(format(user_weight,".2f"),"lb =",format(new_weight,".2f"),"kg")
        

