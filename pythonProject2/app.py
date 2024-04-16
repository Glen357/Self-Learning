# print("Glen Radovan")
# print("o----")
# print(" ||||")

# print("*" * 10)
# These lines simply print some text to the console

# *************************** Variables ************************************************
# price = 10
# rating = 4.9
# name = "Glen"
# is_published = False
#
# print(price)
#The input() function is used to receive input from the user, assigning the input to variables
#
# *********************** Receiving input ****************************************************
# first_name = input("enter your first name: ")
# last_name = input("enter your last name: ")
# new_patient = input("are you a new patient here?: ")
# print(first_name)
# print(last_name)
# print(new_patient)

# 
# birth_year =int(input("enter your birth year: ")) 
# age = 2024 - birth_year 
# print(age)
#
# ************************* Type conversion ****** Moved to converters.py ************************
# it converts a user's input from a string to an integer for calculation
# **************************** Formatted Strings *******************************************
# first ="John"
# last = "Smith"
# # message = first + '[' + last + '] is a coder'
# msg = f'{first} {last} is a coder'
# print(msg)
#  here iuse formatted strings to create strings with variables interpolated

# ************************* Strings and string Methods *************************************************
# course = "Python for Beginners"
# # print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find("o"))
# print(course.replace('Beginners', 'absolute Beginners'))
# print(course)
# print('Python' in course)

# Various string methods 

# ******************************* If Statments ************************************************
# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("drink some water")
# elif is_cold:
#     print("get a jacket")
# else:
#     print("lovely day")
# these statements are used to control the flow of the program based on certain conditions(Conditional statements)

# ****************************** Logical operators *******************************************************
# price = 1000000
# buyer_credit_good = True
#
# if buyer_credit_good:
#     down_payment = 0.1 * price
#     print(f"please make ${down_payment} deposit")
# else:
#     down_payment = 0.2 * price
#     print(f"please make: ${down_payment}")


# has_good_credit = True
# has_criminal_record = False
#
# if has_good_credit and not has_criminal_record:
#     print("eligible for loan")
# here I showed using logical operators in conditional statements


# ***************************** Comparison Operators ********************
# name = "Glen"
# if  len(name) < 4:
#     print("minimum name length 3 letters")
# elif len(name) > 4:
#     print("maximum name length 50 letters")
# else:
#     print("name looks good")
#  I Used these comparisson operators to compare the values of the name variable. I could use this to compare user inputs
# ************************* While Loops *************************
# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print("done")
# While loops are used for repeated execution based on a condition

# ***************************** Building a guessing game wit while Loops *************************
# secret_number = 9
# i = 0 # represents the guess count
# limit = 3
# while i < limit:
#     guess = int(input('guess: '))
#     i += 1
#     if guess == secret_number:
#         print("nailed it!")
#         break
# else:
#     print('Sorry no Luck')
# 
# command = ""
# started = False
#this is a guessing game where the user has to guess a secret number using a while loop and comparisson operators

# ********************************** Building a Car game with what has been Learned so far ******************************************
# while command != "quit":
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("car started")
#     elif command == "stop":
#         if not started:
#             print("Car has already stopped")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print('''
#         start - to start the car
#         stop - to stop
#         quit - to quit
#         ''')
#  this is a car game where the user can start, stop, or get help there is a while loop and comparison operators with if, else and elif statements

# **************************** For Loops **********************************************

# for item in range(5, 10, 2):
#     print(item)

# prices = [10, 20, 30]
# total = sum(prices)
# print(total)
#
# total = 0
# for price in prices:
#     total += price
# print(f"total: {total}")
#                              Nested Loops

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# For loops are used for iterating over sequences of items. below is the print out in the terminal

        # C:\Users\Admin\PycharmProjects\pythonProject2\.venv\Scripts\python.exe
        # C:\Users\Admin\PycharmProjects\pythonProject2\app.py
        # (0, 0)
        # (0, 1)
        # (0, 2)
        # (1, 0)
        # (1, 1)
        # (1, 2)
        # (2, 0)
        # (2, 1)
        # (2, 2)
        # (3, 0)
        # (3, 1)
        # (3, 2)
        #
        # Process
        # finished
        # with exit code 0


#                              Nested Loops 
# numbers = [2, 2, 2, 2, 5]
# for items in numbers:
#     output = ''
#     for item in range(items):
#         output += 'x'
#     print(output)

    # xxxxx
    # xx
    # xxxxx
    # xx
    # xx
# these nested loops create patterns or iterate over varying data structures

# ********************************* Lists *****************************************************
# names = ['john', 'bob', 'mosh', 'sarah', 'mary']
# names [0] = 'jon' # this modified the item in the list
# print(names[2:4])
# print(names)
# list operations can modify the elements of a list

# *****************************************************************************************************
# numbers = [4, 6, 8, 11, 46, 2] # My attempt
# print(max(numbers))
# print(min(numbers))
#
# numbers = [4, 6, 8, 11, 46, 2] # solution example
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)
#
# 46
# 2
# 46
# ********************************** 2D Lists******************************************************
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)
# *********************************  List methods*************************************************
# numbers = [4, 6, 11, 8, 11, 8, 46, 46, 2]
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers)
# print(numbers2)
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# [4, 6, 11, 8, 46, 2]
# ************************************ Turples **********************************************
# numbers = (4, 6, 8, 11, 46, 2)
# numbers[0] = 10
# print(numbers[0]) # outlines that Tuples are immutable, (can't be changed)

# ************************ Unpacking **************************************************
# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print(coordinates)

# the above 2 sections show how tuples are immutable and how they can be used for unpacking

# ***************************** Dictionaries *********************************************************
# 
# customer = {
#     "name" : "John Smith",
#     "age": 30,
#     "is_verified":True
# }
# print(customer["name"])
# print(customer.get("Name"))
# 
# phone_number = input("phone: ")
# digit_map = {
#     '1': 'one',
#     '2': 'two',
#     '3': 'three',
#     '4': 'four'
# }
# output = ' '
# for ch in phone_number:
#     output += digit_map.get(ch, "!") + ' '
# print(output)
#                           Emoji Converter
# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "😀",
#     ":(": "😔"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)
# Dictionaries and their usage, including iterating over keys and values

# *************************** Functions*********************************************************
# def greet_user(first_name, last_name):
#     print(f"hi {first_name} {last_name}")
#     print("welcome aboard")
#
#                                Parameters Key word and positional arguments
# print("start")
# greet_user("John", "smith")
# greet_user("Mary", "Jane")
# print("finish")
#                                        Return Statements 
# def square(number):
#     return number * number
#
# print(square(3))

#                               creating Reusable functions
# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "😀",
#         ":(": "😔"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# message = input(">")
# print(emoji_converter(message))

# ******************************** Exceptions ***************************
# try:
#     age = int(input("age: "))
#     print(age)
# except ValueError:
#     print("Please enter a numeric value")
#     age = int(input("age: "))
#     print(age)
# ************************************************************************************
#                           Introduction to Comments
#*************************************************************************************

# *************************** Classes ****************************************
# class Point:
#     def __init__(self, x, y):
#         self.x = 10
#         self.y = 20
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#                               Constructors
#
# point = Point(10, 20)
# point.x = 11
# print(point.x)

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi I am {self.name}")
#
#
# john = Person("John Smith")
#
# john.talk()
#
# bob = Person("Bob Smith")
# bob.talk()

#     def __init__(self, name, birth_year, talk):
#         self.name = "john"
#         self.birth_year = "1868"
#         self.talk = input("Leave us a message: ")
#
#
# person = Person("name",
#                 "birth_year",
#                 "talk")
# person.name
# person.birth_year
# person.talk
# print(person())
# Classes are defined along with methods(__init__), and objects are created from those classes


# ***************************** Inheritance ***********************************************
# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark")


# class Cat(Mammal):
#     def be_annoying(self):
#         print("be annoying")
#
#
# dog1 =Dog()
# dog1.walk()
# dog1.bark()
# cat1 = Cat()
# cat1.walk()
# cat1.be_annoying()
# Inheritance is used to create subclasses that share behaviours

# **************************************************************************************************
# ****************** Modules and packages **************************

# import converters
# from converters import kg_to_lbs
#
# print(kg_to_lbs(117))
#
# # print(converters.kg_to_lbs(70))


# 
# from Utils import find_max
#
# numbers = [1, 5, 6, 8, 44]
# # max = find_max(numbers)
# print(max(numbers))

# from ecommerce import shipping
#
# shipping.calc_shipping()
# This section is about importing modules and packages and using their functions/variables
# ***************************** IGenerating Random Values***************************************************
import random
#
#
# members = ['John', 'Mary', 'bob', 'Jill']
# leader = random.choice(members)
# print(leader)
# 
# for i in range(3):
#     random.random()
#     print(random.randint(10, 20))

# 
# dice = range(1,6)
# roll = random.choice(dice)
# roll2 = random.choice(dice)
#
# print(roll, ',', roll2)
#
#                               
# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())
# This is to Generate random numbers and choosing random items from a list
# **************************** Working with Directories *****************************************
# from pathlib import Path
#
# path = Path("ecommerce")
# print(path.exists())
# Here I use the pathlib package to work with other directories and files

# ******************************** Automation with Python ******************************************
# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference
#
# def process_workbook(filename):
#
#     wb = xl.load_workbook(filename)
#     sheet = wb['Sheet1']
#
#
#     for row in range(2, sheet.max_row + 1):
#         cell = sheet.cell(row, 3)
#         corrected_price = cell.value * 0.9
#         corrected_price_cell = sheet.cell(row, 4)
#         corrected_price_cell.value = corrected_price
#
#     values = Reference(sheet,
#               min_row=2,
#               max_row=sheet.max_row,
#               min_col=4,
#               max_col=4)
# 
#     chart = BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart, 'e2')
#
#     wb.save(filename)
# this piece showed me how to manipulate Excel files in Python for fast data processing

# ******************************************** Machine Learning *****************************************
