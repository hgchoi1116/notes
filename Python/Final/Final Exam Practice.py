# Final Exam Practice


# 1
# import math
# import random


# def string_work(s1, s2, s3):
#     len_list = [len(s1), len(s2), len(s3)]
#     print(len_list)


# string_work("hello", "hi", "bye")

# 2
def digits_3_5(digit):
    value3 = 0
    value5 = 0
    for char in str(digit):
        if char == "3":
            value3 += 1
        if char == "5":
            value5 += 1
    print(value3, value5)
    return value3, value5


digits_3_5(335552135)

# 3
# def list_dig_sum(list_in):
# sum_int=0
# count_nonneg=0
# count_neg=0
# for value in list_in:
# for digit in str(value):
# if digit.isdigit():
# sum_int+=int(digit)
# if value>=0:
# count_nonneg+=1
# else:
# count_neg+=1
# print(sum_int,count_nonneg,count_neg)
# list_dig_sum([1,24,-34,-5,0,12])

# 4
# def no_end_digit(list_in):
# output=[]
# for element in list_in:
# if not(str(element)[-1].isdigit()):
# output.append(element)
# print(output)
##no_end_digit([12,"yes","best 5","Arthur"])

# # Problem2
# random.seed(22)


# def gen_list():
#     list_random = []
#     for value in range(10):
#         list_random.append(random.randint(100000, 600000))
#     return list_random


# def num_7(list_in):
#     count_7 = 0
#     count_7s = 0
#     for element in list_in:
#         count_7temp = 0
#         for char in str(element):
#             if char == "7":
#                 count_7temp += 1
#         if count_7temp >= 2:
#             count_7s += 1
#         count_7 += count_7temp
#     return count_7, count_7s


# def num_stars(list_in):
#     output_list = []

#     for element in list_in:
#         output_element = ""
#         for char in str(element):
#             output_element += char+"*"
#         output_list.append(output_element[:-1])
#     return output_list


# def two_lists(list_in):
#     list_even = []
#     list_odd = []
#     for element in list_in:
#         if int(element) % 2 == 0:
#             list_even.append(element)
#         else:
#             list_odd.append(element)
#     return list_even, list_odd


# def number(list_in):
#     output = ""
#     for element in list_in:
#         output += str(element)[0]
#     return int(output)


# def main():
#     rand_list = gen_list()
#     print("10 random integers are")
#     print(rand_list)
#     count_7, count_7s = num_7(rand_list)
#     print("Number of 7s in the list: ", count_7)
#     print("Number of at least two digits 7: ", count_7s)

#     print("List in star form")
#     print(num_stars(rand_list))

#     list_even, list_odd = two_lists(rand_list)
#     print("even: ", list_even)
#     print("odd: ", list_odd)

#     print("the first digits of integers: ", number(rand_list))

# # main()


# print(math.e, math.pi)
