##1.        @@ @@@@@
##          $$ $$$$$
##          && &&&&&
##2.    4  --16
##3.    YES
##4.   False
##     True
##5. E
##6. LOW LOW LOW LOW OK
##      OK
##7. 0 1 4 9
##     0 1 4 9 16 25

#Program 1

def factorial(number):
     total=1
     if number!=0:
          for i in range(1,number+1):
               total*=i
     print("factorial of ",number,"is",total)
factorial(0)
factorial(15)

def code(number):
     number=str(number)
     number_new=""
     for i in number:
          if int(i)%2==1:
               number_new+="*$*"
          else:
               number_new+="#"
     print(number_new)

##code(10023)
##code(789456)

def validation(string):
     if len(string)>=6 and len(string)<=10:
          count=0
          for i in string:
               if i=="$" or i=="&":
                    count+=1
          if count>=2:
               print("VALID")
     else:
          print("INVALID")

##validation("12JK&5$11")
##validation("$$G&&")          


#Program2
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

##main()

