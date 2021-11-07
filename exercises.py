#source-Exercises
#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Ex_1-Printing
#Ans_1
#print("Twinkle, twinkle, little star,\n\t\tHow I wonder what you are!\n\t\t\t\t Up above the world so high,\n\t\t\t\t Like a diamond in the sky.\n Twinkle, twinkle, little star, \n\t\t\t\tHow I wonder what you are")

#Ex-2: get python version program

#Ans_2
# import sys
# print(sys.version)
# print(sys.version_info)

#Ex3: print current date and time
# #Ans-3:
# import datetime
# date_time=datetime.datetime.now()
# print("current date and time is :",date_time)
#
# print("formatted date and time is: ", date_time.strftime("%Y-%m-%d %H:%M:%S"))

#Ex-4: take radius inout fromuser and output area

# #ans4:
# from math import pi
# r=float(input("enter the radius of the circle:"))
#
# print("the area of the circle with the radius of ",r, "is :", pi*r**2)
#


#Ex5: Write a Python program which accepts the user's first and last name and
# print them in reverse order with a space between them.

#Ans5:
#
# first_name=str(input("enter your first name:"))
# last_name=str(input("enter your last name:"))
#
#
# print(last_name+" "+ first_name)

#Ex6: Write a Python program which accepts a sequence of comma-separated numbers from user
# and generate a list and a tuple with those numbers.

#Ans6:
# numbers= input("Enter some comma separated numbers")
#
# list=numbers.split(',')
# print("list is:" ,list)
#
# tuple_numbers=tuple(list)
# print("tuple is:",tuple_numbers)

#Ex7:Write a Python program to accept a filename from the user and print the extension of that

#Ans7
#
# file_name=str(input("enter filename with extension"))
#
# filename=file_name.split(".")
# print(filename[-1])
#
# print(repr(filename[-1]))

#Ex-8: Write a Python program to display the first and last colors from the following list. Go to the editor
#color_list = ["Red","Green","White" ,"Black"]

#Ans_8:
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[-1])

#Ex-9: Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
#exam_st_date = (11, 12, 2014)
#Sample Output : The examination will start from : 11 / 12 / 2014

#Ans_9:

# exam_st_date = (11, 12, 2014)
#
# #not efficient way to print
# print(exam_st_date[0],'/',exam_st_date[1],'/',exam_st_date[2])
#
# #efficient way to print
#
# print("Examination will start from: %i/%i/%i"%exam_st_date)

#Ex10:

#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

#Ans10:


# a=input("enter the number")
#
# number1=int("%s" %a)
# number2=int("%s%s"%(a,a))
# number3=int("%s%s%s"%(a,a,a))
#
# print(number1+number2+number3)

#Ex11: Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
#Ans11:
#print(sum.__doc__)

#Ex12:Write a Python program to print the calendar of a given month and year.
#Ans12:

# import calendar
# y= int(input("Input the year:"))
# x=int(input("Input the month:"))
#
# print(calendar.month(y,x))

#ex13:print exercise

#ans13:
#
# print("""
#
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# """)

#Ex14. Write a Python program to calculate number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)

# #Ans14:
# from datetime import date
#
# d1=date(2014,7,2)
#
# d2=date(2014,7,11)
#
# delta=d2-d1
# print(delta)
# print(delta.days)

#ex15: Write a Python program to get the volume of a sphere with radius 6.

# #Ans15:
# from math import pi
# radius=int(input("enter the radius of the sphere:"))
#
# print("The Volume of the sphere is :", 4/3*pi*(radius**3))

#eX16:Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

#Ans16

# number=int(input("Enter a number: "))
#
# def difference(number):
#     if number <=17:
#         return(17-number)
#     else:
#         return(2*abs(17-number))
#
# print(difference(number))

#Ex17:Write a Python program to test whether a number is within 100 of 1000 or 2000

#Ans17:

# number = int(input("Enter the number"))
# def difference_test(n):
#     return (abs(n-1000)<= 100 or abs(n-2000)<=100)
# print(difference_test(number))

#18. Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum

#Ans 18:

# numbers=input("Enter three numbers seperated by comma")
# number_list=[]
#
# numbers_list=[number_list.append(int(i) )for i in numbers.split(',')]
#
# print(number_list)
#
#
# def summation(numbers_list):
#      if numbers_list[0]==numbers_list[1] and numbers_list[1]==numbers_list[2]:
#         return 3*(sum(numbers_list))
#      else:
#          return (sum(numbers_list))
# print(summation(number_list))

#Ex19. Write a Python program to get a new string from a given string where
# "Is" has been added to the front. If the given string already
# begins with "Is" then return the string unchanged.

#Ans19:

# user_string=input("Enter the string:")
#
# if len(user_string)>=2 and user_string[:2]=='Is':
#     print (user_string)
# else:
#     print('Is'+user_string)

#Ex20.  Write a Python program to get a string which is n (non-negative integer) copies of a given string.

# #Ans_20:
# user_string = input(("Enter the string:"))
#
# print(2*user_string)

#Ex21:Write a Python program to find whether a given number (accept from the user) is even or odd,
# print out an appropriate message to the user.

#Ans21:
# number=int(input("enter the number:"))
# mod=number%2
# if mod==0:
#     print("You have entered an even number")
# else:
#     print("You have entered an odd number")

#Ex22: Write a Python program to count the number 4 in a given list.

#Ans22:
# numbers_list=input("enter list of numbers")
# numbers_list=numbers_list.split(",")
#
# for i in range(0,len(numbers_list)):
#     numbers_list[i]=int(numbers_list[i])
#
# print(numbers_list)

#Ex23:Write a Python program to get the n (non-negative integer)
# copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2

#Ans 23:
user_string=input("Enter the string")
n=int(input("enter n"))
if len(user_string)>=2:
    print(n*user_string[:2])
else:
    print(n*user_string)
#change