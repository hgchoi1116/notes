#05052021 LAB

##Theory
##1.  ODA
##2.  NO
##3.  False
##    False
##    False
##    False
##    False
##4.  5,6
##5.  we
##    We like Python
##    PYTHON.
##6.  False
##    3
##    14
##    -1
##    I like Python.
##7.  RACADARACADARACADA
##8.  racadabra    

###Program1
##
##print("This program displays a transformed  form of a positive integer.")
##print("If you enter # for the integer, the program ends.")
##
##
##user_int=input("Enter a positive integer: ")
##string_new=""
##X=0
##Y=0
##while user_int!="#":
##    while not user_int.isdigit():
##        print("The input is not valid.")
##        user_int=input("Enter a positive integer: ")
##
##    if "8" in user_int:
##        print("The number was tranformed to: ",user_int.replace("8","X"))
##        X+=1
##    else:
##        for char in user_int:
##            if int(char)%2!=0:
##                string_new+="Y"
##            else:
##                string_new+=char
##        print("The number was tranformed to: ",string_new)
##        Y+=1
##
##    user_int=input("Enter a positive integer: ")
##
##print("The number of X transformation: ",X)
##print("The number of Y transformation: ",Y)
##
##
##print("This program displays a transformed  form of a positive integer.")
##print("If you enter # for the integer, the program ends.")





#Program2

print("This program displays a new strings created from two entered strings.")
print("To end the program - enter for the first string @@@.")

string_1=input("Enter the first string: ")
string_2=input("Enter the second string: ")

if string_2 in string_1:
    position=string_1.find(string_2)
    before=string_1[:position]
    after=string_1[position+len(string_2):]
    print("before: ",before,"\tafter: ",after)
else:
    print("together: ", string_1,"&",string_2)
    
