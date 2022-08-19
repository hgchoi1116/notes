###Program 1
##
##import random
##
##def work_list():
##    random_list=[]
##    for i in range(12):
##        x=random.randint(1000,1999)
##        random_list.append(x)
##    return random_list
##
##def symbols(random_list):
##    output=[]
##    for value in random_list:
##        if value%10==7 or value%10==9:
##            output.append("$")
##        elif (value%10)%2==0:
##            output.append("%")
##        else:
##            output.append("#")
##    return output
##
##def numbers(random_list):
##    output=[]
##    first_last=[]
##    for value in random_list:
##        last=value%10
##        first=(value//1000)*10
##        output.append(first+last)
##    return output
##
##def main():
##    print("This is a list of random integers:")
##    gen_list=work_list()
##    print(gen_list)
##    print("This is a list of symbols: ")
##    gen_sym=symbols(gen_list)
##    print(gen_sym)
##    print("This is a list of created numbers: ")
##    gen_number=numbers(gen_list)
##    print(gen_number)
##
##main()


#Program2

import random

def temp_day_night():
    first_list=[]
    second_list=[]
    for i in range(10):
        first=random.randint(43,47)
        first_list.append(first)
        second=random.randint(30,34)
        second_list.append(second)
    return first_list,second_list

def temp_ave(list_in):
    list_ave=sum(list_in)/10
    list_count=0
    for value in list_in:
        if value<list_ave:
            list_count+=1
    return list_ave,list_count

def temp_min(list_in):
    minimum=list_in[0]
    output=[]
    for value in list_in:
        if minimum>value:
            minimum=value

    for value in list_in:
        if minimum==value:
            output.append("MIN")
        else:
            output.append(value)
    return minimum, output

def temp_max(list_in):
    maximum=list_in[0]
    output=[]
    for value in list_in:
        if maximum<value:
            maximum=value

    for value in list_in:
        if maximum==value:
            output.append("MAX")
        else:
            output.append(value)
    return maximum, output    

def main():
    print("This program displays info about temperature during a 10-day period.")
    print("")
    
    day,night=temp_day_night()
    print("Temperature info about days: ")
    print("\tThe list of day temperatures: ",day)
    day_avg,day_low=temp_ave(day)
    print("\tThe average day temperature is ",day_avg)
    print("\tThere were",day_low,"days with lower than the average temperature")
    day_min,day_min_list=temp_min(day)
    print("\tThe minimum day temperature is",day_min)
    print("\tThe min occured on following days:",day_min_list)
    day_max,day_max_list=temp_max(day)
    print("\tThe maximum day temperature is",day_max)
    print("\tThe max occured on following days: ",day_max_list)

    print("Temperature info about night: ")
    print("\tThe list of nights temperatures: ",night)
    night_avg,night_low=temp_ave(night)
    print("\tThe average nights temperature is ",night_avg)
    print("\tThere were",night_low,"nights with lower than the average temperature")
    night_min,night_min_list=temp_min(night)
    print("\tThe minimum nights temperature is",night_min)
    print("\tThe min occured on following nights:",night_min_list)
    night_max,night_max_list=temp_max(night)
    print("\tThe maximum nights temperature is",night_max)
    print("\tThe max occured on following nights: ",night_max_list)

    
main()
