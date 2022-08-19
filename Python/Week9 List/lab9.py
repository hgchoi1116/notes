#Hyungeeu Choi

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

