###Theory
##
##1.
##value is: 4
##value is: 6
##value is: 8
##
##2.
##value is: 20
##value is: 18
##value is: 16
##value is: 14
##value is: 12
##
##3.
##I am happy!
##I am happy!
##I am happy!
##I am happy!
##I am happy!
##
##4.
##0
##1
##4
##9
##16
##
##5.
##2*7 = 14
##4*6 = 24
##6*5 = 30
##8*4 FALSE
##
##6.
##1
##4
##7
##10
##count = 4
##
##7.
##0 5 MAYBE
##1 3 MAY
##2 1M
##There were 3 printings.
##
##8.
##ABRA

###Program1
##print("This progrma displays a number of  in strings.")
##print("To end the program enter \"%\" for the string,")
##
##string=input("Enter a string: ")
##string_new=""
##count_total=0
##count_string=0
##count=0
##while string!="%":
##    for position in string:
##        if position=="a":
##            string_new+=position
##            count+=1
##            count_total+=1
##            count_string+=1
##    print("There are", count,"\"a\"-s in the string.")
##    count=0
##    string=input("Enter the next string: ")
##
##print("You entered", count_string,"strings.")
##print("There were",count_total,"\"a\"-s in these strings")
    
##even number characeter = doubling  each character
##odd numberand more than 6 = exchange first two with last two
##odd number character less than 6 = middle character tripled and rest the same

#Program2
#String conversion

print("This program converts strings.")
print("To end the program enter \"!\" for the string.")

string=input("Enter a string: ")
count=0
while string!="!":
    string_new=""
    if len(string)%2==0: #even
        for position in string:
            string_new+=2*position
    elif len(string)>6: #odd more than 6
        for position in range (len(string)):
            if position==0:
                string_new+=string[-2]
            elif position==1:
                string_new+=string[-1]
            elif position==len(string)-1:
                string_new+=string[1]
            elif position==len(string)-2:
                string_new+=string[0]
            else:
                string_new+=string[position]
    elif len(string)<6: #odd less than 6      
        for position in range (len(string)):
             if position==len(string)//2:
                 string_new+=3*string[position]
             else:
                 string_new+=string[position]
    count+=1
    print("The encoded string is:",string_new)
    string=input("Enter the next string: ")
print("You entered",count,"strings.")



