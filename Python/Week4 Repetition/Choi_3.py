#Hyungeeu Choi
#HW3 for Week4

print("This program transforms an integer to a string of Xs and Ys and Ws.")
print("")
user_number=int(input("How many integers do you want to transform?"))
print("")
for number in range(1,user_number+1):
    print("Integer #",number,end=" - ")
    string_new=""
    user_integer=str(input("Enter the integer: "))
    for space in user_integer:
        if space == "-":
            string_new+="W"
        elif int(space)%2==0:
            string_new+="X"
        else:
            string_new+="Y"
    print("The transformed string is",string_new)
    print("")

print("Thank you for using my program!")
