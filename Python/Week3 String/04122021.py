#04122021



###Grading
###Boolean Variables and Flag Variables
##print("This program displays an average score and a grade for three exams.")
##print("")
##alert_grade=False
##alert_ave=False
##
##test_1=float(input("enter your score for test1: "))
##test_2=float(input("enter your score for test2: "))
##test_3=float(input("enter your score for test3: "))
##
##average = (test_1+test_2+test_3)/3
##
##if test_1<60 or test_2<60 or test_3<60:
##    alert_grade=True
##
##if average<70:
##    alert_ave=True
##
##if average>=95:
##    grade="A"
##elif average>=85:
##    grade="B"
##elif average>=70:
##    grade="C"
##elif average>=60:
##    grade="D"
##else:
##    grade="F"
##
##print("Your average score is :", format(average,".2f"))
##print("Your grade is:", grade)
##if alert_grade and alert_ave: #means alert is true
##    print("You have to improve your scores and your average!")
##elif alert_grade:
##    print("Some of your scores are low!")
##elif alert_average:
##    print("Your average score is low!")


###Color Mixer
##print("Enter two different primary colors.")
##color_1=input("Your color#1 (red, blue or yellow) is: ")
##color_2=input("Your color#2 (red, blue or yellow) is: ")
##
##if (color_1=="red" or color_2=="red") and (color_1=="blue" or color_2=="blue"):
##    mix="purple"
##elif (color_1=="red" or color_2=="red") and (color_1=="yellow" or color_2=="yellow"):
##    mix="orange"
##elif (color_1=="blue" or color_2=="blue") and (color_1=="yellow" or color_2=="yellow"):
##    mix="green"
##else:
##    mix="do not know"
##print("")
##print("Your colors are:",color_1,"and",color_2)
##print("")
##print("By mixing these two colors you will get:",mix)


###Menu driven programs
###Cube menu
##
##print("This program dispays the surface area, the volume, or both.")
##print("")
##base=float(input("Enter a length of the base of a cube in centimeters: "))
##surface_area=6*base**2
##volume=base**3
##print("")
##print("if you would like to get the surface area, enter S.")
##print("if you would like to get the volume, enter V.")
##print("if you would like to get the both, enter B.")
##print("")
##
##choice=input("Enter your choice: ")
##print("")
##if choice=="S" or choice=="s":
##    print("The surface area of the cube is",format(surface_area,".2f"))
##elif choice=="V" or choice=="v":
##    print("The volume of the cube is",format(volume,".2f"))
##elif choice=="B" or choice=="b":
##    print("The surface area of the cube is",format(surface_area,".2f"))
##    print("The volume of the cube is",format(volume,".2f"))   
##else:
##    print("There is no such choice in the menu.")
##print("")
##print("Thank you for using my program!")


#strings... more
##                    my_string="Monday or Tuesday!"
##                    print(my_string)
##                    print(my_string[0]) #M #index [] starts with 0
##                    print(my_string[1]) #o
##                    #print(my_string[20]) #out of range
##                    print(my_string[5]) #y
##                    print(my_string[6]) #space
##                    print(my_string[17]) #! #positive means go from left to right
##                    print(my_string[-1]) #! #negative means go from right to left
##
##len                 print(len(my_string)) #18 meaning [0 -17] #len means length of string

##                    string_a="word"
##                    string_b="1234"
##
##                    new_string=string_a[0]+string_a[1]+string_b[0]+string_b[1]
##                    print(new_string)
##
##                    new_string=2*string_a[0]+string_a[1]+string_b[0]+3*string_b[1]
##                    print(new_string) #wwo1222 #multiplying means repeat the same value

##                    number="23"
##
##                    digit1=number[0]
##                    digit2=number[1]
##                    print(digit1, digit2)
##                    print(digit1+digit2) #combining two texts
##                    print(int(digit1)+int(digit2)) #converting to int then calculating as number

#string slicing
##                    your_string="Happy day"
##                    print(your_string[0:4]) #Happ #0 is the start position and 4 is the end position (not included)
##                    print(your_string[0:5]) #Happy
##                    print(your_string[4:7]) #y d
##
##                    string_a="word"
##                    string_b="1234"
##
##                    new_string=2*string_a[0:2]+2*string_b[0:2]
##                    print(new_string)

########################################################################
#04142021

###convert number to string
##y=54
##print(2*y)
##print(str(y)[0]) #str

##string="123abc456"
##new_string=string[0]+'....'+string[-1]
##print(new_string)


###initials
##first=input("Enter your first name: ")
##last=input("Enter your last name: ")
##initial=first[0]+'.'+last[0]+'.'
##print("The initials are: ",initial)

##            #string slicing
##            string="123456ABCDE"
##            print(string[0:6])
##            print(string[2:6])
##            print(string[-5:]) #blank means until the end
##            print(string[0:7:2]) #from position 0 to 7. print every 2nd value
##            print(string[-2:-6:-2]) #from D to A, print every 2nd value
##
##            z=int(string[0:3])+int(string[3:6])
##            print(z)


###string work
##user_str=input("Enter a string: ")
##print("The string has", len(user_str), "characters.")
##print("")
##
##print("Hint: ", user_str[0]+"..."+user_str[-1])
##print("")
##
##if user_str[0]==user_str[-1]:
##    print("The first and the last characters are the same.")
##else:
##    print("The first and the last characters are NOT the same.")


###string, alphabet comparison
##name_1=input("Enter the first name: ")
##name_2=input("Enter the seocnd name: ")
##
##if name_1<name_2:
##    print(name_1,name_2)
##else:
##    print(name_2,name_1)


###Strings with seven characters
##print("This program displays portions of a string.")
##user=input("Enter a string with seven characters: ")
##if len(user)==7:
##    user_elimiated=user[1:6]
##    user_middle=user[3]
##    user_update=user[:3]+"X"+user[-3:]
##    print("The string with first and last characters missing is:", user_elimiated)
##    print("The middle character is: ", user_middle)
##    print("The modified string is: ", user_update)
##else:
##    pring("wrong input")


###Middle characters in strings
##
##print("This program displays middle characters of a string.")
##user=input("Enter a string:")
##
###pattern
###abc (3) - b (1)
###abcde (5) - c (2)
###abcdefg (7) - d (3)
###length//2 is middle character
###abcd (4) - bc [1:3]
###abcdef (6) -cd [2:4]
###abcdefgh (8) - de [3:5]
###length//2 -1 and +1
##
##if len(user)%2==0:
##    i=len(user)//2-1
##    j=len(user)//2+1
##    middle=user[i:j]
##else:
##    i=len(user)//2
##    middle=user[i]
##print("The middle characters are: ",middle)

    
