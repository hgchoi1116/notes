# TEST 2 NOTE

#string validation
while not user_in.isdigit():# "-" sign in string is not a digit
    print("THis is not a valid input!")
    user_in=input("Enter a positive integer: ")

##string modification
#split method
word="abrakadabra"
word_list=word.split("a")

print(word_list) #splits word in a

#count vowel
vowels="aeiou"
user_string=input("Enter a string: ")
count_vowels=0

for char in user_string:
    if char in vowels:
        count_vowels+=1

#test
string.isalnum() #contain only alphabetic letters or digits
string.isalpha()
string.isdigit()
sting.islower()
string.isupper()
string.isspace() #whitespace characters ie space \w \t
#modification
string.lower()
string.upper()
string.lstrip() # remove all leading whitespace characters
string.lstrip(char)
string.rstrip #right side
string.rstrip(char)
string.strip() #removes all leading and trailing spaces
string.strip(char) #beginning or ending that matches char is removed
#search and replace
string.endswith(substring) #returns true
string.find(substring) #returns lowest index
string.replace(old,new)
startswith(substring) #returns true

#for loop
score=input("Enter your score separated by spaces: ")
score_list=score.split()
print(score_list)

print("Your individual scores are: ")
for score in score_list:
    print(score)

#while loop
while user_number!=0:
    final+=user_number
    if user_number>0:
        right+=1
    else:
        left+=1
    user_number=float(input("Enter the next move: "))

#calling a function
#function displays a number of digits in a string - 1215 S Moutingview Rd
def main():
     info()
     user_text=input("Enter a text:  ")
     while user_text!="%":
          num_digit(user_text)
          print("")
          user_text=input("Enter the next text: ")
     print("")
     print("Thank you for using my program!")
     
def info():
     print("This program displays a number of digits in a text.")
     print("To end the program enter \"%\" for the input.")

def num_digit(text):
     count=0
     for char in text:
          if char.isdigit():
               count+=1
     print("Digits: ", count)
