###Part II. Programming
###Program 1
##celcius = float(input('Enter a temperature in Celcius: '))
##fahrenheit = (9/5)*celcius+32
##print(format(celcius,'.2f'),'degree C =',format(fahrenheit,'.2f'),'degree F')
##
###Program 2
##min = int(input('Enter min: '))
##sec = int(input('Enter sec: '))
##
##totalmin = min + sec/60
##totalhour=totalmin/60
##
##speed = 6/totalhour
##
##print(format(speed,'.2f'),'miles/hour')
##

#Hyungeeu Choi
#a program that asks the user to provide a two digit integer and
#displays the individual digits and the sum of digits
user_int=int(input('enter two digit integer: '))

digit_ten=user_int//10
digit_one=user_int%10 

print('Digits are:',digit_ten,',',digit_one)
print('The sum of digits is: ', digit_ten+digit_one)
