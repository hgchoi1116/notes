#W2 Classwork


##    # Taxi Cost
##
##    print("This program displays a charge from a taxi company.")
##
##    #constants
##    SERVICE_FEE=10
##    MILE_FEE=1.2-
##    TAX=0.101
##    TIP=0.15
##
##    UserMile=float(input("Enter the distance you want to travel: "))
##    print('')
##
##    #calculations
##    TaxiCost=SERVICE_FEE+MILE_FEE*UserMile
##    TaxUser=TaxiCost*TAX
##    TipUser=TaxiCost*TIP
##    total=TaxiCost+TaxUser+TipUser
##
##    print("You will pay: ")
##    print("taxi cost: \t$",format(TaxiCost,'5.2f'))
##    print("state tax: \t$",format(TaxUser,'5.2f'))
##    print("tip: \t\t$",format(TipUser,'5.2f'))
##    print('-------------------------')
##    print("Total: \t\t$", format(total,'5.2f'))


##    #Calculations with MATH module
##
##    import math
##    print("This program calculated charges for an on-line shopping.")
##
##    SHIPPING_BOX=1.35
##    TAX=.101
##    ITEM_PRICE=1
##    BOX_CAPACITY=10
##
##    NumberItem=int(input("Enter the number of items to buy: "))
##
##    #calculation
##    item_cost=NumberItem*ITEM_PRICE
##    shipping_user=math.ceil(item_cost/BOX_CAPACITY)*SHIPPING_BOX
##    tax_user=(item_cost+shipping_user)*TAX
##    total=item_cost+tax_user+shipping_user
##
##    print("All items:\t$",format(item_cost,"8.2f"))
##    print("shipping :\t$", format(shipping_user,"8.2f"))
##    print("tax: \t\t$", format(tax_user,"8.2f"))
##    print("Total Price:\t$", format(total,"8.2f"))


##                #decision structure
##
##                temperature=float(input("Enter the temperature outisde: "))
##
##                #making decision
##                if temperature<=40:
##                    print("Take a coat!")
##                else:
##                    print("You don't need a coat, it is warm outside!")
##                print("Thank you")


##                #if-else Even vs Odd
##
##                print("This program displays whether the integer is even or odd.")
##                integer_user=int(input("Enter an integer: "))
##                if integer_user%2==0: #== is equal    != is not equal
##                    print("The integer is an even number.")
##                else:
##                    print("The integer is an odd number.")


##                # Other way if-elif-else
##
##                print("This program displays whether the number is in the given interval.")
##                number=float(input("Enter your number: "))
##
##                if number>100:
##                    print("The number is OUT.")
##                elif number>=25:
##                    print("The number is IN.")
##                else:
##                    print("The number is OUT.")

##                # AND OR NOT boolean expression
##                print("THis program displas whether the number is in the given interval.")
##                number=float(input("Enter your number: "))
##                if number>=25 and number<=100:      #AND
##                    print("The number is IN.")
##                else:
##                    print("The number is OUT.")
##
##                if number<25 or number>100:         #OR
##                    print("The number is OUT.")   
##                else:
##                    print("The number is IN.")
##
##                if not(number>=25 and number<=100): #NOT
##                    print("The number is OUT.")
##                else:
##                    print("The number is IN.")

    
##    #Password test
##
##    system_password="SUMMER2021"
##    log_in=input("Enter your password: ")
##
##    if system_password==log_in:
##        print("You are in.")
##    else:
##        print("Incorrect Password.")
##    #Cost of copies
##    print("a program that asks the user the number of copies and displays the total cost in dollars.")
##
##    copy=int(input("Enter number of copies: "))
##
##    if copy<=100:
##        cost=copy*0.05
##    else:
##        cost=((copy-100)*0.03)+5
##    print("The cost is $", format(cost,"0.2f"),".")


##    #number in an interval (25-100)
##
##    print("This program displays whether the number is in the given interval.")
##    number=float(input("Enter your number: "))
##
##    if number<=100:
##        if number>=25:
##            print("the number is IN.")
##        else:
##            print("the number is OUT.")
##    else:
##        print("The number is out.")


##    #Buy one get one 50% off sale
##
##    item1=float(input("Enter the price for the fist item:$ "))
##    item2=float(input("Enter the price for the 2nd item:$ "))
##
##    if item1>item2:
##        cost=item1+(.5*item2)
##    else:
##        cost=(.5*item1)+item2
##
##    print("The total price is $", format(cost,"0.2f"))


##    #Shipping Charges
##
##    weight=float(input("What is the weight of your package? "))
##
##    if weight>10:
##        cost=weight*4.75
##    elif weight>6:
##        cost=weight*4
##    elif weight>2:
##        cost=weight*3
##    else:
##        cost=weight*1.5
##
##    print("The shipping cost for your package is $",format(cost,"0.2f"),".")


#Chocolate Bar

print("This program displays whether it is possible to get required number of squares by splitting the chocolate on only one time.")

n=int(input("Enter the number of rows: "))
m=int(input("Enter the number of columns: "))
square=int(input("Enter the number of chocolate squares: "))

if n*m>square:
    if square%n==0 or square%m==0:
        print("You can get your number of chocolates in one break.")
    else:
        print("You cannot get your number of chocolates in one break.")
else:
    print("You entered the number of squares that are bigger than the size of the chocolate.")
    
