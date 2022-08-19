# TCSS141 - 21Q1_FE practice

# PROBLEM#1 - functions

def string_work(str1,str2,str3):
    len_list=[len(str1),len(str2),len(str3)]
    print(len_list)
string_work('I am happy!','Today','1256')


def digits_3_5(number):
    dig_3=0
    dig_5=0
    for char in str(number):
        if char=='3':
            dig_3+=1
        elif char=='5':
            dig_5+=1
    return dig_3,dig_5
    #print(dig_3,dig_5)
#digits_3_5(-12533654789.123)


def list_dig_sum(list_in):
    dig_sum=0
    count_0_pos=0
    count_neg=0
    
    for integer in list_in:
        if int(integer)>=0:
            count_0_pos+=1
            for dig in str(integer):
                dig_sum+=int(dig)
        else:
            count_neg+=1
            integer=str(integer)[1:]
            for dig in str(integer):
                dig_sum+=int(dig)
    return dig_sum,count_0_pos,count_neg
    #print(dig_sum,count_0_pos,count_neg)
#list_dig_sum([2,-100,-151,0,555])

def no_end_digit(list_in):
    list_out=[]
    for element in list_in:
        if not str(element)[-1].isdigit():
            list_out.append(element)
    #return list_out
    print(list_out)
no_end_digit([12,'12 S.st','Big 5',-152])


# PROBLEM #2 - program with functions

import random
random.seed(22)

def main():
    print('')
    rand_list=gen_list()
    print('A): This is the list of generated random numbers: ')
    print(rand_list) 

    print('')
    seven,more_sevens=num_7(rand_list) 
    print('B) The digit "7" is in the generated list',seven,'times.')
    print(' In the generated list are',more_sevens,'integers with at least two digits "7" in.')
   
    print('')
    star_list=num_stars(rand_list) 
    print('C) This is the list of "star" numbers: ')
    print(star_list)
    
    print('')
    rand_even,rand_odd=two_lists(rand_list)
    print('D) This is the list of even random integers: ')
    print(rand_even)
    print('   This is the list of odd random integers: ')
    print(rand_odd)

    print('')
    num_created=number(rand_list) 
    print('E) This is the created number: ',num_created)
    
    
def gen_list():
    list_out=[]
    for i in range(10):
        x=random.randint(100000,600000)
        list_out.append(x)
    return list_out

    
def num_7(list_in):
    count_7=0
    count_7_more=0
    for integer in list_in:
        int_7=0
        for digit in str(integer):
            if int(digit)==7:
                int_7+=1
        count_7+=int_7
        if int_7>=2:
            count_7_more+=1
            
    return count_7,count_7_more
    #print(count_7,count_7_more)
#num_7([115522,557779,723456])


def num_stars(list_in):
    list_out=[]
    for integer in list_in:
        int_star=''
        for digit in str(integer):
            int_star+=digit+'*'
        list_out.append(int_star[:-1])
    return list_out
    #print(list_out)
#num_stars([115522,557779,723456])


def two_lists(list_in):
    list_even=[]
    list_odd=[]
    for integer in list_in:
        if integer%2==0:
            list_even.append(integer)
        else:
            list_odd.append(integer)
    return list_even,list_odd
    #print(list_even,list_odd)
#two_lists([115522,557779,723456])

def number(list_in):
    num_out=''
    for number in list_in:
        num_out+=str(number)[0]
    return num_out
    #print(num_out)
#number([115522,557779,723456])
    
main()
        
