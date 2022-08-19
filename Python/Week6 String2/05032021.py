#05032021
#validation

#valid number of hours not more than 60
##while hours<0 or hours>60:
##    print("The number of entered hours is not valid")
##    hours=float(input("Enter the valid number of hours: "))

##hours=float(input("Enter the number of worked hours: "))
##
##while hours<0 or hours>60:
##    print("The number of entered hours is not valid")
##    hours=float(input("Enter the valid number of hours: "))
##weekly_pay=hours*17.5
##print("The weekly pay is: $", format(weekly_pay,".2f"))

###multiple inputs for number of hours using SENTINEL
##hours=float(input("Enter the number of worked hours: "))
##while hours!=0: #SENTINEL
##    while hours<0 or hours>60: #VALIDATION
##        print("The number of entered hours is not valid")
##        hours=float(input("Enter the valid number of hours, not 0: "))
##    weekly_pay=hours*17.5
##    print("The weekly pay is: $", format(weekly_pay,".2f"))
##    hours=float(input("Enter the valid number of hours: "))


# more about strings

##string_1="ABCD"
##string_2="AB"
##print("A" in string_1) # output is "True"
##
##if string_2 in string_1:
##    print("The character AB is in string_1")
##else:
##    print("The character AB is not in the string.")

###SEE CH8_more about strings PG.3
##string_A="mix 123"
##string_B="1235"
##string_C="wRRt"
###.isalnum() is True when variable ONLY contains letters or digits
##print(string_A.isalnum()) #False
##print(string_B.isalnum()) #True
##print(string_C.isalnum()) #True
###.isalpha() is True when variable ONLY contains letters
##print(string_A.isalpha()) #False
##print(string_B.isalpha()) #False
##print(string_C.isalpha()) #True
###.isdigit() is True when variable ONLY contains digits
##print(string_A.isdigit()) #False
##print(string_B.isdigit()) #True
##print(string_C.isdigit()) #False
###.islower() is True when variable ONLY contains lower case
##print(string_A.islower()) #True
##print(string_B.islower()) #False
##print(string_C.islower()) #False
###.isupper() is True when variable ONLY contains upper case
##print(string_A.islower()) #False
##print(string_B.islower()) #False
##print(string_C.islower()) #False
###.isspace() is True when variable only whitespace (space, \n,\t)
##print(string_A.isspace()) #False


###SEE CH8_more about strings PG.4
##string_A="mix 123"
##string_B="1235"
##string_C="wRRt"
###.upper() returns all characters in UPPERCASE
##print(string_A.upper()) #MIX 123
##print(string_B.upper()) #1235
##print(string_C.upper()) #WRRT
##
###lstrip(char) removes char at the begginning
###Also known as left side strip
##print(string_A.lstrip("m")) #MIX 123


###SEE CH8_more about strings PG.5
#string_A="mix 123"
##string_B="1235"
##string_C="wRRt!"
##
##print(string_A.endswith("23")) #True
##print(string_B.startswith("23")) #False
##print(string_C.endswith("Rt")) #False
##
##print(string_A.find("23")) #5
##print(string_B.find("25")) #-1 = not found
##print(string_C.find("R")) #1
##
##print(string_A.replace("23","8888")) #5
##print(string_B.replace("25","x")) #-1 = not found
##print(string_C.replace("R","$$")) #1


###Class Exercises
##
##user=input("Enter your created password: ")
##
##length=False
##upper=False
##lower=False
##digit=False
##
##if len(user)>=8:
##    length=True
##
##for char in user:
##    if char.isupper():
##        upper=True
##    if char.islower():
##        lower=True
##    if char.isdigit():
##        digit=True
##if length and upper and lower and digit:
##    print("Your password is valid.")
##else:
##    print("Your password is not valid.")


###Digits in a string
##
##user=input("Enter a string: ")
##
##digit_in=False
##
##for char in user:
##    if char.isdigit():
##        digit_in=True
##
##while user!="0" and digit_in:
##    digit_in=False
##
##    for char in user:
##        if char.isdigit():
##            digits_in=True
##        
##    user_number=0
##    user_sum=0
##    user_digit=""
##    for char in user:
##        if char.isdigit():
##            user_number+=1
##            user_sum+=int(char)
##            user_digit+=char
##    print("The number of digits in the string: ",user_number)
##    print("The sum of digits: ",user_sum)
##    print("The digits in the string: ",user_digit)
##    user=input("Enter a string: ")


#############################################################
#############################################################
###05052021
### Validation
##
##user_in=input("Enter a positive integer: ")
##
##while not user_in.isdigit():# "-" sign in string is not a digit
##    print("THis is not a valid input!")
##    user_in=input("Enter a positive integer: ")
##
##print(int(user_in)**2)


###String modification
###word Separator
###normal sentence
##sentence=input("Enter a sentence in a strange form: ")
##
##normal=""
##normal+=sentence[0]
##
##for index in range(1,len(sentence)):
##    if sentence[index].isupper():
##        normal+=" " + sentence[index].lower()
##
##    else:
##        normal+=sentence[index]
##
##print(normal)


###String searching
###Vowel in a string using in method
##
##vowels="aeiou"
##user_string=input("Enter a string: ")
##count_vowels=0
##
##for char in user_string:
##    if char in vowels:
##        count_vowels+=1
##print(count_vowels)


###String searching
###Decimal Places
##
##user_string=input("Enter a float: ")
##i=user_string.find(".")
##
###method 1 for loop
##string="."
##count=0
##for char in range(user_string.find(".")+1,len(user_string)):
##    string+=user_string[char]
##    count+=1
##print(string)
##print(count)
##
###method 2 slicing (way shorter)
##j=user_string[i:]
##print(user_string[i:])
##print(len(j)-1)


#split method

word="abrakadabra"

word_list=word.split("a")
test=""
for word in word_list:
   test+=word
print(word_list)
print(test)
##
##my_value=[1,2,3,4,5]
##for element in my_value:
##    print(element)
##
##for element in range(1,6):
##    print(element)


###average value of scores
##
##score=input("Enter your score separated by spaces: ")
##score_list=score.split()
##print(score_list)
##
##print("Your individual scores are: ")
##for score in score_list:
##    print(score)
##
##total=0
##for score in score_list:
##    total+=float(score)
##
##
##average=total/len(score_list)
##print("Total: ", format(total,".2f"))
##print("Average: ", format(average,".2f"))
##print("The second score:",score_list[1])


##my_list=["Adam", "Eva", "Sophia", "Tom"]
##
##for index in range(len(my_list)):
##    print(my_list[index])
##
##print(my_list[1:3])


###Creating a list [1,4,9,16,25]
##my_list=[]
##for value in range(1,6):
##    square=value**2
##    my_list.append(square) #append -add element after element
##print(my_list)
##print(sum(my_list))

##
##str_list=["3","5","7"]
##
##num_list=[]
##for value in str_list:
##   num_list.append(int(value))
##
##print(num_list)
##print(sum(num_list))
