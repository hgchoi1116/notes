#Hyungeeu Choi


print("This program displays positions of the entered points.")

user_int=int(input("How many points do you want to provide? "))

for i in range (1,user_int+1):
    print("")
    print("The point #",i,":")
    x=float(input("Enter the x coordinate of the point P: "))
    y=float(input("Enter the y coordinate of the point P: "))
    if x!=0 and y!=0:
        if x>0:
            if y>0:
                position="in the quadrant I"
            else:
                position="in the quadrant IV"
        elif x<0:
            if y>0:
                position="in the quadrant II"
            else:
                position="in the quadrant III"
    else:
        if x==0 and y==0:
            position="on the origin"
        elif x==0:
            position="on the axis y"
        else:
            position="on the axis x"
    print("")
    print("The point (",format(x,".1f"),",",format(y,".1f"),") is",position,".")

print("")
print("")
print("Thank you for using my program!")
