###05102021
##
###calling a function
##
##def even_odd_digits():
##    integer=input("Enter a positive integer: ")
##    count_even=0
##    count_odd=0
##    for digit in integer:
##        if int(digit)%2==0:
##            count_even+=1
##        else:
##            count_odd+=1
##    print(count_even,"even digits in the integer.")
##    print(count_odd,"odd digits in the integer.")
##
###even odd digits()


##def main():
##    print("This program displays first and last names of people.")
##    repetition=int(input("How many names do you want to enter? "))
##    print("")
##    for value in range(repetition):
##        first_name()
##        last_name()
##        print("")
##
##def first_name():
##    user_name=input("Enter a full name (in the form first space last): ")
##    space=user_name.find(" ")
##    first=user_name[:space]
##    print("The first name is: ",first)
##
##def last_name():
##    user_name=input("Enter a full name (in the form first space last): ")
##    space=user_name.find(" ")
##    last=user_name[space+1:]
##    print("The last name is: ",last)
##
###main()


###functions with parameters
##
##def main():
##    print("This program displays the first and last name.")
##    print("")
##    user_name=input("Enter the full name: ")
##    print("")
##    first_name(user_name)
##    last_name(user_name)
##
##def first_name(name_in): #name_in = a parameter   Jason Choi = argument
##    #user_name=input("Enter a full name (in the form first space last): ")
##    space=name_in.find(" ")
##    first=name_in[:space]
##    print("The first name is: ",first)
##
###first_name("Jason Choi")
##
##def last_name(name_in):
##    #user_name=input("Enter a full name (in the form first space last): ")
##    space=name_in.find(" ")
##    last=name_in[space+1:]
##    print("The last name is: ",last)
##    
###last_name("Jason Choi")
##
##main()

##def main():
##    print("This program changes a string.")
##
##    user_str=input("Enter a string: ")
##    vowels_up(user_str)
##    
##def vowels_up(string_in):
##    string_out=""
##    vowels="aeiou"
##    for char in string_in:
##        if char in vowels:
##            string_out+=char.upper()
##        else:
##            string_out+=char
##    print("The new string is: ", string_out)
##
##main()


##COEFFICIENT=5  #global
##def main():
##    print("This program displays surface and volume of a cube")
##    print("")
##    user_base=input("Enter the base of the cube: ") #local
##    print("")
##    cube_surface(user_base)
##    cube_volume(user_base)
##
##def cube_surface(base):
##    surface=6*float(base)**2 #local
##    print("The surface area is: ", surface)
##
##def cube_volume(base):
##    volume=float(base)**3 #local
##    print("The volume is: ", volume)
##
##main()


##def ave_value(number1,number2):
##    average=(number1+number2)/2
##    print("The average value is: ", average)
##
##ave_value(12.5,48.3)
    
    
#####################################################################
#####################################################################

#05122021

###function displays a number of digits in a string - 1215 S Moutingview Rd
##def main():
##     info()
##     user_text=input("Enter a text:  ")
##     while user_text!="%":
##          num_digit(user_text)
##          print("")
##          user_text=input("Enter the next text: ")
##     print("")
##     print("Thank you for using my program!")
##
##def info():
##     print("This program displays a number of digits in a text.")
##     print("To end the program enter \"%\" for the input.")
##
##def num_digit(text):
##     count=0
##     for char in text:
##          if char.isdigit():
##               count+=1
##     print("Digits: ", count)
##
##
##main()


###String Validation
##
##def valid_str(text):
##     space=text.find(" ")
##     letter=text[:space]
##     number=text[space+1:]
##     if space!=-1 and letter.isalpha() and number.isdigit():
##          print("Valid format")
##     else:
##          print("Invalid format")
##          
##valid_str("ab cd") 
##valid_str("abcd 45") #valid
##valid_str("123 abc")
##valid_str("abc123")


###Sum of First n Numbers Function with a Parameter
##
##def main():
##     
##     info()
##     
##     user_in=int(input("Enter a positive integer: "))
##     count_n=0
##     while  user_in>0:
##          total_n(user_in)
##          count_n+=1
##          print("")
##          user_in=int(input("Enter the next number: "))
##     print("")
##     print("The number of displayed sums: ", count_n)
##     print("Thank you!")
##
##def info():
##     print("The program displays the sum of first n positive integers.")
##     print("Enter 0 or a negative integer to end the program.")
##
##def total_n(n):
##     count=1
##     total=0
##     while count<=n:
##          total+=count
##          count+=1
##     print("Total=", total)
##     
##main()

###Grading
##def grade(e1,e2,e3):
##     average=(e1+e2+e3)/3
##     if average>=90 and average<=100:
##          grade="A"
##     elif average>=80:
##          grade="B"
##     elif average>=70:
##          grade="C"
##     elif average>=60:
##          grade="D"
##     else:
##          grade="F"
##
##     print("Average score: ", format(average,".1f"))
##     print("Grade: ",grade)
##
##grade(90.3,75.1,81.6)

###t1=10% t2=20% fe=30%
##
##def course_tests(t1,t2,fe):
##     average=t1*.1+t2*.2+fe*.3
##     print("Your tests contribution is" average,"to your exams.")
##
##course_tests(100,100,100)

     
#Insurance Charge

def main():

     info()

     label=input("Enter a container label: ")

     while label.upper()!="END":
          premium(label)
          print("")
          label=input("Enter a container label: ")

     print("Thank you for using my program.")          

def info():
     print("This program displays a charge for an insurance.")
     print("The valid label is in the form size-value.")
     print("To end the program, enter \"END\" for the label.")

def premium(label):
     label_new=label.upper()
     label_size=label_new[:2]
     label_value=label_new[3:]
     valid_label=False
     if ((label_size=="SM" or label_size=="LG")  and label[2]=="-" and label_value.isdigit()):
          label_value=int(label_value)
          if label_size=="SM":

               if label_value<=10000:
                    cost=50
               else:
                    cost=label_value*.005
          else:
               if label_value<=10000:
                    cost=90
               else:
                    cost=label_value*.009
          print("The insurance charge is $",format(cost,".2f"))
     else:
          print("NOT valid label")

main()
