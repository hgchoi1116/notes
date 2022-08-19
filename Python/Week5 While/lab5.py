#Hyungeeu Choi

print("This progrma displays a number of  in strings.")
print("To end the program enter \"%\" for the string,")
print("")
string=input("Enter a string: ")
string_new=""
count_total=0
count_string=0
while string!="%":
    count=0
    for position in string:
        if position=="a":
            string_new+=position
            count+=1
            count_total+=1  
    print("There are", count,"\"a\"-s in the string.")
    count_string+=1
    string=input("Enter the next string: ")

print("You entered", count_string,"strings.")
print("There were",count_total,"\"a\"-s in these strings.")
    
