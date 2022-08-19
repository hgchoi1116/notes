#Hyungeeu Choi

def main():
    functionA()
    functionB()
    functionC()

def functionA():
    print("***function A")
    print("")
    is_valid(104)
    print("")
    is_valid(516)
    print("")
    is_valid(221)
    print("")

def is_valid(number):
    if number>=100 and number<=500 and number%4==0:
        print("The number",number, "is VALID.")
    else:
        print("The number",number, "is INVALID.")


#FUNCTION B

def functionB():
    print("***function B")
    print("")
    num_words("Today is a beautiful day!")
    print("")
    num_words("Hello!")
    print("")
    
def num_words(sentence):
    count=0
    for char in sentence:
        if char==" ":
            count+=1
    word=count+1

    print("The sentence is: ",sentence)
    print("The sentence has",word,"words.")



#FUNCTION C

def functionC():
    print("***function C")
    print("")
    digit_sum(2135)
    print("")
    digit_sum(-168)
    print("")
    digit_sum(-47101)

def digit_sum(number):
    total=0
    for i in str(number):
        if i.isdigit():
            total+=int(i)
    print("The entered integer is: ",int(number))
    print("The sum of digits is: ",total)

main()

