#Program2 lab4.py
#Hyungeeu Choi
print("This program displays info about the entered positive integer.")
user_int=int(input("Enter a positive integer: "))
even=0
odd=0
for digit in str(user_int):
    if int(digit)%2==0:
        even+=1
    else:
        odd+=1

print("There are",even,"even digits.")
print("There are",odd,"odd digits.")
