#Final Exam Note

#string validation for positive number
while not user_in.isdigit():# "-" sign in string is not a digit
    print("This is not a valid input!")
    user_in=input("Enter a positive integer: ")

#split method
word="abrakadabra"
word_list=word.split("a")

#in function
vowel="aeiou"
for char in user_string:
    if char in vowels:
        count_vowels+=1
