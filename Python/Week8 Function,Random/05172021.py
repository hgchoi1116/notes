#05172021

###value returning functions
##
##def main():
##    user_str=input("Enter a string: ")
##    user_hint=hint(user_str) #receiving the return
##
##    print(user_hint)
##
##
##def hint(string_in):
##    string_out=string_in[0]+"..."+string_in[-1]
##    #print(string_out)
##    return string_out #RETURNING!!!!
##
###hint("Adam")
##main()


##def main():
##    print("This program displays earning of workers.")
##
##    worker_hours=int(input("Enter the number of hours worked: "))
##
##    while worker_hours!=0:
##        work_pay=pay(worker_hours)
##        print("This worker's pay is $", work_pay)
##        print("")
##        worker_hours=int(input("Enter the number of hours worked: "))
##
##def pay(hours):
##    hourly_rate=15
##    worker_pay=hours*hourly_rate
##    return worker_pay
##
##main()


#returning more values @@@@@@@@@@@@@@@@@@@@@@@@@

##def main():
##
##    my_base=5
##
##    my_surface,my_volume=cube(my_base) #receiving TWO values
##
##    print("The surface area of my cube is: ",my_surface)
##    print("The volume of my cube is: ",my_volume)
##
##def cube(base):
##    cube_surface=6*base**2
##    cube_volume=base**3
##
##    return cube_surface, cube_volume # returning TWO values
##
##main()

##def main():
##    print("This program displays average value of two numbers.")
##    
##    x=float(input("Enter the first number: "))
##    y=float(input("Enter the second number: "))
##    while not (x==0 and y==0):
##        my_ave=ave_two(x,y)
##        print("The average value is ", my_ave)
##        
##        x=float(input("Enter the first number: "))
##        y=float(input("Enter the second number: "))
##def ave_two(num_1,num_2):
##    ave_value=(num_1+num_2)/2
##    return ave_value
##
##main()


####Class exercises

###Savings
##
##import math
##INT_RATE=0.005
##
##def main():
##    print("This program displays the saving on your bank account.")
##    print("To end the program enter 0 for the initial deposit.")
##    principal=float(input("Enter the principal: "))
##
##    while principal>0:
##        time=float(input("Enter the number of years: "))
##        saving=savings(principal,INT_RATE,time)
##        print("Your future value on your account is $: ",format(saving,".2f"))
##        print("")
##        principal=float(input("Enter the principal: "))        
##
##def savings(principal,rate,time):
##    amount=principal*math.exp(rate*time)
##    return amount
##
##main()


#####################################################################
#RANDOM VALUES

##import random #random numbers
##random.seed(7) #not random, sequence
##
##for i in range(15):
##    x=random.randint(1,10) #random integer between 1 and 10
##    print(x, end=" ")
##print("")
##
##for i in range(25):
##    x=random.randrange(1,10,2) #random range between 1 and 9 jumping two (1,3,5,7,9)
##    print(x, end=" ")
##print("")


##import random
##random.seed(11)
##
##def random_val(n): #n represents a number of integers (1,10), sum, ave
##    total=0
##    for i in range(n):
##        x=random.randint(1,10)
##        total+=x
##        print(x, end=" ")
##    print("")
##    print("The sum of values is: ",total)
##    ave_value=total/n
##    print(format(ave_value,".2f"))
##
##random_val(5)

import random
random.seed(11)

def main():
    print("This program displays problems to practice on.")
    more="YES"
    count_pract=0
    count_correct=0
    while more.upper()=="YES":
        count_pract+=1
        my_answer=mult_practice()
        if my_answer:
            count_correct+=1
        more=input("Do you want more practice? (YES/NO) ")
    print("You worked on ",count_pract,"exercises.")
    print("You answered",count_correct,"exercises correct.")
def mult_practice():
    correct=False
    x=random.randint(1,15)
    y=random.randint(1,15)
    print(x,"x",y,"=")
    z=int(input("Enter the answer: "))
    if x*y==z:
        print("Correct!")
        correct=True
    else:
        print("Incorrect!")
        print("The correct answer is: ",x*y)

    return correct
main()

##import math
##
##def main():
##    radius=float(input("Enter the radius: "))
##    while radius>0:
##        circum,area=circle(radius)
##        print("type A to display circumference")
##        print("type B to display area")
##        print("type C to display both")
##        choice=input("Enter your choice: ")
##        if choice=="A":
##            print("circumference= ",format(circum,".2f"))
##        elif choice=="B":
##            print("area = ",format(area,".2f"))
##        elif choice=="C":
##            print("circumference=: ",format(circum,".2f"))
##            print("area = ",format(area,".2f"))
##        else:
##            print("There is no such choice in the menu")
##        
##        radius=float(input("Enter the radius: "))
##        
##def circle(radius):
##    circum=math.pi*2*radius
##    area=math.pi*radius**2
##    return circum, area
##
##main()
