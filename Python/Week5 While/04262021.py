#04262021

###While Loop
### While Condition
##
##more="yes"
##time=0
##while more=="yes": #while the condition is true
##    print("We are the best!")
##    time+=1
##    more=input("Do you want more printing? (yes/no) ") #change the condition
##print("")
##print("The statement was displayed",time,"times.")


###average value of entered numbers
##more="yes"
##total=0 # for sum
##count=0 # numbers
##
##while more=="yes":
##    number=float(input("Enter a number for the sum: "))
##    total+=number
##    count+=1
##    
##    more=input("Do you want more printing? (yes/no) ")
##print("")
##average = total/count
##
##print("average =", format(average, ".2f"))


##for i in range(15,7,-4): #same product "for" and "while"
##    print(i)
##print("")
##k=15
##while k>7:
##    print(k)
##    k-=4


###sum of first n positive integers
##more="Y"
##count_sum=0
##while more=="Y":
##    
##    user_in=int(input("Enter a positive integer: "))
##    count_sum+=1
##    total=0
##    
##    for i in range(1,user_in+1):
##        total+=i
##    print("")
##    print("1+2+...+",user_in,"=",total)
##    
##    more=input("Do you want more printing? (Y/N) ")
##print("The program displayed", count_sum,"summations.")


###First name Anna Small -> Anna
##
##full_name=input("Enter a full name: ")
##
##first_name=""
##
##position=0
##
##while full_name[position]!=" ":
##    first_name+=full_name[position]
##    position+=1
##print("")
##print(first_name)
    

#############
#04282021
#############

##number=10
##while number>4:
##    print(number)
##    number-=2

##more="Y"
##while more=="Y":
##    user_int=int(input("Ener an integer: "))
##    print(user_int**2)
##    more=input("again Y/N?")


###List of squares
##
##user_int=int(input("Enter a positive integer: "))
##base=0
##while base**2<=user_int:
##    print(base**2,end=",",)
##    base+=1
##print("")


##word="today"
##part_word="" #tod
##position=0
##
##while position<len(word) and word[position]!="m":
##    part_word+=word[position]
##    position+=1
##
##print(part_word)


###Budget Analysis
##print("This program displays the amount that the user is over or under budget")
##budget=float(input("What is your budget? "))
##
##total=0
##
##condition="Y"
##i=1
##while condition=="Y":
##    spend=float(input("Spending #1: "))
##    total+=spend
##    condition=input("More Y/N?")
##
##flag==false
##if budget>total:
##    
##difference=budget-total
##
##if budget>total:
##    print(difference,"\tUnder Budget")
##elif budget<total:
##    print(difference,"\tOver Budget")
##else:
##    print("You are on point")

################
### SENTINEL
################
###sum of numbers with a sentinel 0
##
##print("This program displays the sum of entered numbers.")
##print("To end the program enter 0 for the number.")
##
##total=0
##user_number=float(input("Enter a number: "))
##
##while user_number!=0:
##    total+=user_number
##    user_number=float(input("Enter the next number: "))
##
##print("") 
##print("The sum of numbers is: ", format(total,".2f"))


###Budget with SENTINEL
##print("This program displays the amount that the user is over or under budget")
##budget=float(input("What is your budget? "))
##
##total=0
##
##condition="Y"
##print("Enter your expenses and enter 0 when done")
##spend=float(input("Expense: "))
##while spend!=0:
##    spend=float(input("Expense: "))
##    total+=spend
##difference=budget-total
##
##if difference<=0:
##    print("You are good")
##else:
##    print("You need to cut down on your expense")


###First name Anna Small -> Anna
###with repetition and sentinel #
##full_name=input("Enter a full name: ")
##while full_name!="#":
##    first_name=""
##    position=0
##
##    while full_name[position]!=" ":
##        first_name+=full_name[position]
##        position+=1
##    print("")
##    print("The first name is: ",first_name)
##    print("")
##    full_name=input("Enter a full name: ")
##print("")
##print("Thank you for using my program!")


###Move along with sentinel
##print("By entering numbers, you can move an object along the axis x.")
##print("The starting position of the object is at zero.")
##print("If you enter a positive number, the object shifts to the right.")
##print("If you enter a negative number, the object shifts to the left.")
##print("By entering 0, you end the shifting.")
##
##user_number=float(input("Enter the move of the object: "))
##final=0
##right=0
##left=0
##
##while user_number!=0:
##    final+=user_number
##    if user_number>0:
##        right+=1
##    else:
##        left+=1
##    user_number=float(input("Enter the next move: "))
##
##print("")
##print("You made",right,"moves to the right;")
##print("You made",left,"moves to the left;")
##print("The final position of the object is x=",final)
        

#Morning Jog - Practice

print("This program displays the number of day needed for the practice.")
print("")

now=int(input("How many miles you can run now? "))
goal=int(input("How many miles you need to run during the event"))

print("")
print("The following table displays how your running skills are improving:")
print("")
day=0

print("DAY OF PRACTICE\t\t\tYOUR RUNNING SKILLS")
while now<=goal:
    day+=1
    now*=1.1
    print("\t",day,"\t\t\t\t",format(now,".2f"))
    
print("")
print("To reach the goal, you need",day,"days to practice.")
