#Hyungeeu Choi
#Program3 SSN Form

print("This program displays nine digit number to SSN format.")

number=input("Enter nine digit number: ")

if len(number)==9:
    SSN=number[:3]+"-"+number[3:5]+"-"+number[5:]
    print("SSN: ",SSN)
else:
    print("You have NOT entered nine digit number")
