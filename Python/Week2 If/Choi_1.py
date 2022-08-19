#Hyungeeu Choi
#Homework1 Online Discount

#constant
CHOCOLATE=1.99
TAX=.101

#input
number_choco=int(input("Enter the number of chocolates to buy: "))

#calculation1
cost_choco=number_choco*CHOCOLATE
shipping= 1.75+((number_choco-1)*.1)

#discount
if cost_choco>=75:
    tax = (cost_choco*.9*TAX)
    discount = cost_choco*.1*-1
    shipping=0
elif cost_choco>=50:
    shipping=0
    tax = cost_choco*TAX
    discount=0
else:
    tax= (cost_choco+shipping)*TAX
    discount=0

#calculation2
total=cost_choco+discount+shipping+tax

#output
print("Purchase: \t$",format(cost_choco,"12.2f"))
print("Discount: \t$",format(discount,"12.2f"))
print("Shipping: \t$",format(shipping,"12.2f"))
print("Tax: \t\t$",format(tax,"12.2f"))
print("---------------------------------------------")
print("TOTAL: \t\t$",format(total,"12.2f"))


