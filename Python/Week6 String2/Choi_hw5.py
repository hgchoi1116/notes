#Hyungeeu Choi

print("This program creats login names and temporary passwords.")
print("By entering \"NONE\" for the name you end the program.")

name=input("Enter the name of the customer in the form: last, first (put a space after \",\"): ")

while name.upper()!="NONE":
    digit=input("Enter the six digit identification number of the customer: ")
    print("")
    name_last=name[:name.find(",")]
    name_first=name[name.find(" ")+1:]
    if len(name_last)>5:
        login=name_last[:5]+digit[:2]
    else:
        placement=len(name_last)
        login=name_last+digit[:7-placement]

    print("The login name is: ", login)

    initial=name_first[0]+name_last[0]
    password=initial.upper()+"$"+digit[-3:]

    print("The temporary password is: ", password)
    print("")
    name=input("Enter the next name of the customer in the form: last, first: ")
