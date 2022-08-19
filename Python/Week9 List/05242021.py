# list methods

# my_list=[2,4,6,8,10,12,14,16]  #bracket for creating a list
# print(my_list[1])
# print(len(my_list)) #5 element = length is 5
# print(my_list)
##
# same_list=list(range(2,18,2)) #list is a type of data
# print(same_list)


##import random
# random.seed(84)
##
# new_list=[]
##
# for i in range (10):
# x=random.randint(1,15)
# new_list.append(x)
##
# print(new_list)


##import random
# random.seed(48)
##
# def main():
##    print("This program works with random lists.")
##    user_n=int(input("Enter the number of elements in the list: "))
##
# user_list=rand_list(user_n)
##
##    print("The created list is: ")
# print(user_list)
##
##    user_ave= ave_list(user_list)
# print(format(user_ave,".2f"))
##
# user_rem6=rem_6(user_list)
# print(user_rem6)
##
##
##
# def rand_list(n): #number of element, 10-50
# list_out=[]
# for i in range(n):
# x=random.randint(10,50)
# list_out.append(x)
##
# return list_out
##
# def ave_list(list_in):
# total=0
# for element in list_in:
# total+=element
# total=sum(list_in) #short cut for adding all the elements
# ave_value=total/len(list_in)
##
# print(ave_value)
# return ave_value
##
# def rem_6(list_in):
# list_out=[]
# for element in list_in:
# r=element%6
# list_out.append(r)
# return list_out
##
# def spec_rem(list_in,rem):
# total=0
# for element in list_in:
# if element==rem:
# total+=1
# print(total)
# return total
##
# spec_rem([1,0,0,2,5,4],0)
# main()


# Class Exercise

# Recursive List
def main():
    print("This program displays a list created recursively.")

    initial = int(input("Enter the first element: "))
    number = int(input("Enter the number of elements to create: "))

    user_list = rec_list(initial, number)
    print("The created list is: ")
    print(user_list)


def rec_list(init, n):
    list_out = [init]

    for i in range(1, n):
        list_out.append(2*list_out[i-1]+3)  # RECURSIVE
    return list_out


main()


# my_list=[5,10,12,45,100,22,45,33]
# print(my_list)
##
# my_list.insert(2,99) #insert (position,value)
# print(my_list)
##
# print(my_list.index(45)) #index(value) returns smallest position, if not found, returns ERROR
##
# if 105 in my_list: #to avoid error use if-else statement
# print(my_list.index(105))
# else:
##    print("There is no 105,")
##
# while 45 in my_list: #to remove all 45s in the list
# my_list.remove(45) #remove(value) removes smallest position value
# print(my_list)
##
# my_list.sort() #sort smallest to largest
# print(my_list)
##
# print(min(my_list)) #lowest value in the list
# print(max(my_list)) #highest value in the list
##
# del my_list[2] #delete position 2
# print(my_list)
##
# our_list=[]+my_list # copy of the list  - first way
##
# my_tuple=tuple(my_list) #list->tuple cannot be editted - second way
##
# value_tuple=(1,2,3)
# value_list=list(value_tuple) #tuple->list edittable
# print(value_list)
# value_list.remove(3) #do not combine it with "print"
# print(value_list)


# score - in %, string 89,98,79,52,10
# def ave_score (score_string):
# score_list=score_string.split(",")
# print(score_list)
##
# score_list_numbers=[]
# for element in score_list:
# score_list_numbers.append(int(element))
# print(score_list_numbers)
##
# ave_original=sum(score_list_numbers)/len(score_list_numbers)
# print(ave_original)
##
# x=min(score_list_numbers)
# score_list_numbers.remove(x)
# ave_original=sum(score_list_numbers)/len(score_list_numbers)
# print(ave_original)
# ave_score("88,12,45,11")


# GAMES
# Number "3" in a die game

# import random

# def main():
#     print("In this game, you guess number of \"3\".")

#     user_r=int(input("How many times the die should be rolled? "))

#     count_game=0
#     count_win=0

#     while user_r>0:
#         count_game+=1
#         user_guess=int(input("Enter your guess about number of \"3\": "))
#         game_list,game_3=die_roll(user_r)
#         print("This is the output of the game: ")
#         print(game_list)
#         if game_3==user_guess:
#             print("You are the winner!")
#             count_win+=1
#         else:
#             print("The computer is the winner!")
#         user_r=int(input("How many times the die should be rolled now? "))
#     print("")
#     print("You played ",count_game, "games.")
#     print("You won ",count_win,"games.")
# def die_roll(r):
#     list_out=[]
#     count_3=0
#     for i in range(r):
#         x=random.randint(1,6)
#         if x==3:
#             count_3+=1
#         list_out.append(x)
#     return list_out,count_3

# main()
