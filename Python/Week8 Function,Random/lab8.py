#Hyungeeu Choi

def main():
    print("This program calculates calrories from fat and carbohydrates.")
    fat=float(input("Enter the number of fat grams consumed today: "))
    carb=float(input("Enter the number of carb grams you consumed today: "))
    print("Calories from fat: ", format(cal_fat(fat),".1f"))
    print("Calories from carbs: ",format(cal_carb(carb),".1f"))
    print("The total number calories is ",format(cal_fat(fat)+cal_carb(carb),".1f"))
    
def cal_fat(fat):
    return fat*9

def cal_carb(carb):
    return carb*4

main()
