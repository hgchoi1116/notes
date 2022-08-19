#05262021

###Theory
##1.  12
##2.  [0,2,4,6,8,10]
##3.  [2 3 4 5 6]
##4.  [5,7,3,10,0,2,1,4,5]
##     10
##     [5,7,3]
##5.     [5,7,4,0,2,1,4,5]
##        [5,4,1,2,0,4,7,5]
##        [5,4,1,2,0,4,7,5]
##        [0,1,2,4,4,5,5,7]
##        [7,5,5,4,4,2,1,0]
##6.    [5,7,4,0,2,1,4,5]
##        [5,7,0,2,1,4,5]
##        [5,7,2,1,4,5]
##7.     [1,8,12,16]
##8.      ["15","12","125"]
##        "1512125"


###Program#1
###Hyungeeu Choi

import random

def main():
    print("This program displays two lists and a sum list.")
    print("To end the program, enter a non-positive number from the number of elements in generated lists.")
    print("")
    n=int(input("Enter the number of elements in generated lists: "))

    while n>0:
        list1,list2=two_lists(n)
        print("The generated lists are: ")
        print(list1)
        print(list2)
        print("")
        list3=sum_list(list1,list2)
        print("The sum list is: ")
        print(list3)
        print("")
        n=int(input("Enter the number of elements in generated lists: "))    
        

def two_lists(n):
    list1=[]
    list2=[]
    for i in range(n):
        list1.append(random.randint(1,50))
        list2.append(random.randint(1,50))
    return list1,list2

def sum_list(list1,list2):
    list3=[]
    for i in range(len(list1)):
        list3.append(list1[i]+list2[i])
    return list3

main()

#Program2
import random

def main():
    print("In this game, you guess the sum of numbers in a die rolling.")
    print("To end the game - enter 0 or a negative number for the number of rolls.")

    n=int(input("How many times the die should be rolled? "))
    game=0
    win=0
    while n>0:
        game+=1
        user_guess=int(input("What is your guess about the sum of numbers? "))
        computer_list,total=computer_roll(n)
        print("This is the output of the game: ")
        print(computer_list)
        print("The sum of numbers is ",total,".")
        if user_guess==total:
            print("You are the winner!")
            win+=1
        else:
            print("The computer is the winner!")
        print("")
        n=int(input("How many times the die should be rolled now? "))
    print("")
    print("You played the game",game,"times, you won ",win,"times.")
    print("Thank you for playing with me!")
    
def computer_roll(n):
    computer_list=[]
    for i in range(n):
        computer_list.append(random.randint(1,6))
    total=sum(computer_list)
    return computer_list,total

main()
