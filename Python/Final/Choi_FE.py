#Hyungeeu Choi
#Final Exam

import random
random.seed(1)

def rand_list():
    output=[]
    for i in range(10):
        x=random.randint(1000,9999)
        output.append(x)
    return output

def even_odd(list_in):
    even=0
    odd=0
    for element in list_in:
        if element%2==0:
            even+=1
        else:
            odd+=1
    return even, odd

def two_lists_info(list_in,N):
    list_small=[]
    list_large=[]
    condition=False
    if N in list_in:
        condition=True
    for element in list_in:
        if element<N:
            list_small.append(element)
        elif element>N:
            list_large.append(element)
    return condition,list_small,list_large

def red_blue_white(list_in):
    output=[]
    for element in list_in:
        if int(str(element)[0])%2==0 and int(str(element)[-1])%2==0:
            output.append("RED")
        elif int(str(element)[0])%2==1 and int(str(element)[-1])%2==1:
            output.append("BLUE")
        else:
            output.append("WHITE")
    return output

def list_new(list_in):
    list_new=[]
    for element in list_in:
        list_new.append(str(element)[0]+"x"+str(element)[-1])
    return list_new

def multi_x(list_new):
    list_multi=[]
    for element in list_new:
        x=int(str(element)[0])*int(str(element)[-1])
        list_multi.append(x)
    return list_multi

def main():
    print("A) This is the list of generated random integers: ")
    work_list=rand_list()
    print(work_list)
    print("")
    print("B)")
    even,odd=even_odd(work_list)
    print("In the generated list are",even,"even integers.")
    print("In the generated list are",odd,"odd integers.")
    print("")
    user_int=int(input("C) Enter a positive integer: "))
    print("")
    condition,list_small,list_large=two_lists_info(work_list,user_int)
    if condition:
        print("INFO: The integer",user_int,"is in the generated list.")
    else:
        print("INFO: The integer",user_int,"is in not the generated list.")
    print("")
    print("This is the list of smaller integers than the entered value:")
    print(list_small)
    print("")
    print("This is the list of larger integers than the entered value:")
    print(list_large)
    print("")
    print("D) This is the list of colors:")
    print(red_blue_white(work_list))
    print("")
    print("E) The \"x\" list is:")
    print(list_new(work_list))
    print("")
    print("F) The list of multiplication is:")
    print(multi_x(work_list))
    print("")
    print("G) This is the list of colors: ")
    print(red_blue_white(work_list))
    
main()
