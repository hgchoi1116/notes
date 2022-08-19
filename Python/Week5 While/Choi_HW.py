#Hyungeeu Choi

print("This program displays factorial of an entered number")
print("")
condition="yes"
count_factorials=0

while condition=="yes":
    user_int=int(input("Enter an integer: "))
    count=1
    answer=1

    if user_int==0:
        print(user_int,"!=",1)
        count_factorials+=1
    elif user_int<0:
        print("Factorial of a negative integer doesn't exist!")
    else:
        while count<=user_int:
            answer*=count
            count+=1
        count_factorials+=1
        print(user_int,"!=",answer)
    
    print("")
    condition=input("Do you want to calculate more factorials? (yes/no) ")

print("The program displayed",count_factorials,"factorials.")
print("Thank you for using my program!")
