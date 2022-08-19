# 04192021

# repetition structure
# for loop
##
# word="HAPPY"
# print(word)
# print("")
# print(word[0])
# print(word[1])
# print(word[2])
# print(word[3])
# print(word[4])
##
# print("")

# [] means list
# for value in [0,1,2,3,4]: #prints position 0, then 1, ...
# print(word[value])

# for element in [2,4,6,8,10]:
# print(element**2)

# for string in ["Peter", "Eva", "Adam"]:
#     print(string[0])
#     print(string[-1])
#     print("")
# print("Thank you!")

# Salary Increase
# salary = 47450
# print("Year # 0 \t\tSalary $", format(salary, ".2f"))
# for i in [1, 2, 3, 4, 5]:
#     salary = salary*1.03
#     print("Year #", i, end="\t\t")
#     print("Salary $", format(salary, ".2f"))


# using a range
# for value in range(5): #[0,1,2,3,4]
# print(value)
# for value in range(1:5) #[1,2,3,4]
# print(value)
# for value in range(10,17):
# print(value)

# word="HAPPY"
# print(word)
# print("")
# for position in range(5):
# print(word[position])

# Salary Increase
# salary=47450
# print("Year # 0 \t\tSalary $",format(salary,".2f"))
# for i in range(1,21):
# salary=salary*1.03
# print("Year #", i, end="\t\t")
##    print("Salary $", format(salary,".2f"))

# for value in range(5,11,2):
##                            print(value, "",end="")
# print("")
# for value in range(5,1,-2):
# print(value,"",end="")


# Average Value
# total=0
# for value in [1,2,3]:
##    number=float(input("Enter a number: "))
# total+=number
# print("")
##print("The sum of entered numbers are", format(total,".1f"))
##print("The average number is", format(total/3,".2f"))
##
# Average of numbers specified by the user
##print("This program displays an average value of entered numbers.")
##user_num=int(input("How many numbers do you want to enter? "))
# total=0
# for value in range(1,user_num+1):
##    number=float(input("Enter a number: "))
# total+=number
# print("")
##print("The sum of entered numbers are", format(total,".1f"))
##print("The average number is", format(total/user_num,".2f"))


# Number of spaces
##print("This program displays a number of spaces in the sentence.")
##string=input("enter a sentence: ")
# total_spaces=0
# for value in range(len(string)):
# if string[value]==" ":
# total_spaces+=1
##print("There are",total_spaces,"spaces in the sentence.")


# Number of spaces different way
##print("This program displays a number of spaces in the sentence.")
##string=input("enter a sentence: ")
# total_spaces=0
##
# for value in string:
# if value==" ":
# total_spaces+=1
##print("There are",total_spaces,"spaces in the sentence.")


# Sum of first n positive integers
##print("This program displays the sum of first n positive integers.")
##user_integer=int(input("Enter a positive integer n:"))
# total=0
# for i in range (1,user_integer+1):
# total+=i
# print(total)
# print("1+2+...+",user_integer,"=",total)


# First of last digit in integer
# positive=0
# negative=0
##user_number=int(input("How many integers do you plan to enter?"))
# for i in range (user_number):
##    user_integer=int(input("Enter a positive or a negative integer: "))
# if user_integer>=0:
##        print("The first digit of integer is",str(user_integer)[0])
# positive+=1
# else:
##        print("The last digit of integer is", str(user_integer)[-1])
# negative+=1
##
##print("Positive Number:",positive)
##print("Negative Number:",negative)


# Multiplication Table
##user_number=int(input("How many integers do you plan to enter?"))
# for value in range (1,user_number+1):
# print("")
##    print("This table displays a multiples of an entered integer.")
##    user_integer=int(input("Enter the integer for multiplication: "))
# print("")
# for i in range (1,11):
# print(user_integer,"x",i,"=",user_integer*i)


# strings
# string="MONDAY"
##
# for position in range(len(string)):
# print(string[position])
##
# different way to do same thing
# for character in string: #going through each character
# print(character)


# creating a new string, replace a A with x
##
user_number = int(input("How many strings do you want to enter?"))

for x in range(user_number):
    string = input("Enter a string: ")
    change = 0
    string_out = ""
    for char in string:
        if char == "a" or char == "A":
            string_out += "*x*"
            change += 1
        else:
            string_out += char
    print(string_out)
    print("Number of Changes:", change)


# Sum of digits
##
##print("This program displays the sum of digits in an entered positive integer.")
##
##user_int=int(input("Enter a positive integer:"))
# total=0
# for digit in str(user_int):
# total+=int(digit)
##
##print("The sum of digits is",total)

# Multiplication Table
##print("This program displays the multiplication table from 11 to 15.")
##
# for i in range (11,16):
# for j in range(11,16):
##        print(i,"x",j,"=",i*j, end="  ")
# print("")

# Double Saving every day
##user_int=int(input("Enter the number of days of saving: "))
# saving=0.01
# total=0
# for i in range(1,user_int+1):
# total+=saving
# print("Saving for the day #",i,"   \t$\t",saving)
# saving*=2
##
# print("")
##print("The total saving for",i,"days is $",format(total,".2f"))


# Integer transformation
# print("This program displays a transformation of an entered integer")
# user_int = str(input("Enter inter:"))
# string_new = ""
# for i in user_int:
#     if i == "-":
#         string_new += "*"
#     elif int(i) % 2 == 0:
#         string_new += "E"
#     elif int(i) % 2 == 1:
#         string_new += "O"
#     else:
#         string_new += " "
# print(string_new)
