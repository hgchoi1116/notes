#Review

#Binary to Decimal

##def bin_dec(bin_in):
##    bin_in=str(bin_in)
##    place=len(bin_in)-1
##    total=0
##    for i in bin_in:
##        total+=int(i)*2**place
##        place-=1
##    return total
##
####def bin_dec(bin_in):  #professor way
####    bin_str=str(bin_in)
####    n=len(bin_str)
####    dec_value=0
####    for i in range(n):
####        dec_value+=int(bin_str[i])*2**(n-1-i))
####    return dec_value
##
##def input_validation(string_in):
##    valid=True
##    for char in string_in:
##        if not(char=="0" or char=="1" or char==" "):
##            valid = False
##    return valid
##
##def bin_list(str_in):
##    bin_list=str_in.split() #blank in () means space; creates a list in string
##    bin_value_list=[]
##    for value in bin_list:
##        bin_value_list.append(int(value)) #converting string to integer
##    return bin_value_list
##
##def main():
##    print("This program transforms binary values to decimal values.")
##    user_bins=input("Enter binary strings separated by spaces: ")
##
##    user_validation=input_validation(user_bins)
##    
##    if user_validation:
##        user_bin_list=bin_list(user_bins)
##        print("The binary list is: ",end=" ")
##        print(user_bin_list)
##        decimal_list=[]
##        for value in user_bin_list:
##            decimal = bin_dec(value)
##            decimal_list.append(decimal)
##        print("The decimal list is: ",end=" ")
##        print(decimal_list)
##    else:
##        print("These are not binary strings")
##
##main()

import random

def coin_toss(t):
    coin_list=[]
    count_head=0

    for i in range(t):
        x=random.randint(0,1)
        if x == 0:
            count_head+=1
            coin_list.append("H")
        else:
            coin_list.append("T")
    print(coin_list, count_head)

coin_toss(100)
    
def main():
    print("In this game, you guess a number of heads.")
    print("If you enter 0 for the number of tosses, the game ends.")

    user_tosses=int(input("How many times the coin should be tossed?"))
    account=0
    
    while user_tosses>0:
        user_H=int(input("How many heads are in the game? "))
        game_list,game_H=coin_toss(user_tosses)
        print("This is the output of the game:")
        print(game_list)
        print("There are",game_H,"heads in the game, your guess was",user_H)

        if user_H==game_H:
            print("You are the winner!")
            account+=1.5
        else:
            print("The computer is the winner!")
            account-=1
        user_tosses=int(input("How many times the coin should be tossed?"))

main()
    
