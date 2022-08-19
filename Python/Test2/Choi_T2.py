#Hyungeeu Choi

def info():
    print("This program displays info about a production of flooring squares.")
    print("The material for flooring squares is received from multiple suppliers.")
    print("The valid material size is in the form: lengthxwidth")
    print("The valid material price is entered as a positive integer.")
    print("The program ends by entering 0 for the size of material.")

def floor_squares(user_in,price):
    x=user_in.find("x")
    length=user_in[:x]
    width=user_in[x+1:]

    if not length.isdigit() and not width.isdigit():   #validation
        print("The size or the price information is not valid.")
    elif not price.isdigit() and price.find(".")>0:
        print("The size or the price information is not valid.")
    else:
        print("The supplied material: LENGTH:",length,"inch, WIDTH:",width,"inch.")
        length=int(length)
        width=int(width)
        price=float(price)
        square_length=length//12
        square_width=width//12
        total_square=square_length*square_width
        print("From the material can be made", total_square,"floor squares.")

        min_price=price/total_square
        print("The minimum price of each square is $",format(min_price,".2f"))

        total_inch=total_square*144
        total_supply=length*width
        not_used=(1-(total_inch/total_supply))*100
        print("Not used material:",format(not_used,".2f"),"%.")

def main():
    info()
    print("")
    material=input("Enter the size of the material to use: ")
    while material!="0":
        price=input("Enter the price of the material: $ ")
        floor_squares(material,price)
        print("")
        material=input("Enter the size of the material to use: ")
    print("")
    print("Thank you for using my program!")

main()
