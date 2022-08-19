#Hyungeeu Choi
#a program that asks the user to provide a two digit integer and
#displays the individual digits and the sum of digits

user_int=int(input('enter two digit integer: '))

digit_ten=user_int//10
digit_one=user_int%10 

print('Digits are:',digit_ten,',',digit_one)
print('The sum of digits is: ', digit_ten+digit_one)
