#Hyungeeu Choi

def main():
    user_in=int(input("Enter a positive integer: "))
    count=0
    while user_in>0:
        code(user_in)
        count+=1
        user_in=int(input("Enter a positive integer: "))
    print("")
    print("You entered",count,"positive integers.")
    print("Thank you for using my program!")
          
def code(number):
     number=str(number)
     number_new=""
     for i in number:
          if int(i)%2==1: #odd
               number_new+="#"
          else: #even
               number_new+="*$*"
     print(number_new)

main()
