#Hyungeeu Choi
#PROBLEM: Practice of operations

import random

def main():
    print("This program provides exercises for practicing integer division \nor finding a remainder.")
    print("")
    print("If you would like to practice integer division, enter 1.")
    print("If you would like to practice remainders, enter 2.")
    print("")
    choice=int(input("Enter your choice: "))
    print("")
    count_exercises=0
    count_correct=0
    if choice==1:
        print("This program tests your skills to do integer division")
        more="YES"
        while more.upper()=="YES":
            count_exercises+=1
            if int_division():
                count_correct+=1
            more=input("Do you want more exercises? (yes/no) ")
        
    elif choice==2:
        print("This program tests your skills to find the remainder.")
        more="YES"
        while more.upper()=="YES":
            count_exercises+=1
            if remainder():
                count_correct+=1
            more=input("Do you want more exercises? (yes/no) ")
    else:
        print("Your choice is not valid")

    print("You made",count_exercises,"exercises.")
    print("Your answer was correct",count_correct,"times.")

        
def int_division():
    dividend=random.randint(-50,50)
    divisor=random.randint(1,10)
    count_correct=False
    print(dividend,"//",divisor,"=")
    user=int(input("Enter your answer: "))
    if dividend//divisor==user:
        print("You are correct!")
        count_correct=True
    else:
        print("You are incorrect!")
        print("The correct answer is",dividend//divisor)

    return count_correct

def remainder():
    dividend=random.randint(-50,50)
    divisor=random.randint(1,10)
    count_correct=False
    print(dividend,"%",divisor,"=")
    user=int(input("Enter your answer: "))
    if dividend%divisor==user:
        print("You are correct!")
        count_correct=True
    else:
        print("You are incorrect!")
        print("The correct answer is",dividend%divisor)

    return count_correct
main()
