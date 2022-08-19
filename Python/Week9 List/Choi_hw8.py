# Hyungeeu Choi

import random

def rand_list(n):
    user_list=[]
    for i in range(n):
        user_list.append(random.randint(10,5000))
    return user_list

def sum_digits(user_list):
    user_sum=[]
    for i in user_list:
        i_str=str(i)
        total=0
        for i in i_str:
            total+=int(i)
        user_sum.append(total)
    return user_sum

def change_list(user_list):
    user_change=[]
    for element in user_list:
        temp=""
        for digit in range(len(str(element))):
            if int(str(element)[digit])%2==1:
                digit="Y"
            else:
                digit="X"
            temp+=digit
        user_change.append(temp)
    return user_change

def num_xy(user_change):
    x=0
    y=0
    for element in user_change:
        for i in range(len((element))):
            if element[i]=="X":
                x+=1
            else:
                y+=1
    return x,y

def main():
    print("This program works with random lists.")
    print("To end the program, enter for the number of elements 0 or a negative integer")

    n=int(input("Enter the number of elements in the random list: "))

    while n>0:
        print("The generated list of random integers is: ")
        user_list=rand_list(n)
        print(user_list)
        print("")
        
        print("The list of digit sum is: ")
        user_sum=sum_digits(user_list)
        print(user_sum)
        print("")
        
        print("The list of strings is: ")
        user_change=change_list(user_list)
        print(user_change)
        print("")

        x,y=num_xy(user_change)
        print("The number of X's in the list is: ",x)
        print("The number of Y's in the list is: ",y)
        print("")
        n=int(input("Enter the next number of elements in the random list: "))

main()
