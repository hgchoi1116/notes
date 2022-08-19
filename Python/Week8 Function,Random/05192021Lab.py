###LAB
##
##1.  no
##2. 5
##3.  14
##    12
##4.  1
##    4
##    9
##    16
##5.  -5
##    -3
##    3
##    13
##    27
##6. 7
##    11
##    6


###Program1
###Hyungeeu Choi
##
##def main():
##    print("This program calculates calrories from fat and carbohydrates.")
##    fat=float(input("Enter the number of fat grams consumed today: "))
##    carb=float(input("Enter the number of carb grams you consumed today: "))
##    print("Calories from fat: ", format(cal_fat(fat),".1f"))
##    print("Calories from carbs: ",format(cal_carb(carb),".1f"))
##    print("The total number calories is ",format(cal_fat(fat)+cal_carb(carb),".1f"))
##    
##def cal_fat(fat):
##    return fat*9
##
##def cal_carb(carb):
##    return carb*4
##
##main()

#Program2
import random

def main():
    n=int(input("Enter the number of integers in the sequence: "))
    count=0
    while n>0:
        count+=1
        average,count_zero=sequence(n)
        print("The average value of sequence is ",format(average,".1f"))
        print("There are",count_zero,"zeros in the sequence.")
        print("")
        n=int(input("Enter the number of integers in the next sequence: "))
    print("")
    print(count,"sequences were created.")
    print("Thank you for using my program!")
            
def sequence(n):
    total=0
    count_zero=0
    for x in range(n):
        x=random.randint(0,10)
        print(x, end=" ")
        total+=x
        if x==0:
            count_zero+=1
    print("")
    average=total/n

    return average,count_zero

main()
    
