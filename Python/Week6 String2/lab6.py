#Hyungeeu Choi

print("This program displays a new strings created from two entered strings.")
print("To end the program - enter for the first string @@@.")

string_1=input("Enter the first string: ")


while string_1!="@@@":
    string_2=input("Enter the second string: ")
    if string_2 in string_1:
        position=string_1.find(string_2)
        before=string_1[:position]
        after=string_1[position+len(string_2):]
        print("before: ",before,"\tafter: ",after)
    else:
        print("together: ", string_1,"&",string_2)
    print("")
    string_1=input("Enter the next first string: ")
    
