print("Hello Kalwe!")

#Keywords in Python: words that are reserved for use in python (about 35 of them). Examples:
# is
# and
# True
# False
# None
# if
# for
# while
# finally
# class
# def

# Rules for naming variables:
# 1. A variable name can not contain space,...
# # erro-> my name/
# 2 ways: i. using CamelCase eg myName...... ii. snake_type eg my_name
# 2. Any one word is permissible in name i.e. age, gender, sex
# 3. They can not start with a number
# 4. they can not contain special characters

#create a variable that stores a persons biodata

name = "Kalwe"
print(type(name))
age = 30
print(type(age))
gender = "male"
married = True
print(type(married))
name = "Johnston"
print(name)

# print(age)
# print(gender)
# print(married)
print([name, age, gender, married])

# Various data types in python:
# * Strings-- refers to a sequence of characters, i.e., abc.... use a single or double quotes
# *
#Strings (Indexing...access an individual character in a string...
z = "I love programming"
new_var=z[0]
print(new_var)
#Slicing String... access characters from a given range..
new_var=z[9:] #does not specify the end of the range
new_var=z[9:16] #specifying the value after the colon, the end character of the range is not included
print(new_var)


y= "learning python program is no joke"
print(len(y))
new_var=y[9:-4]  #-ve counts from the right leftwards
print(new_var)

#string
my_colleague = "valentine"
x=my_colleague.capitalize()
print(x)
y=x.lower()
print(y)

#Exercises
#1. Write a Python program to calculate the length of a string.

y = "learning python programming is no joke!"
print(len(y))

#2. Write a Python program to count the number of characters (character frequency) in a string.
y = "learning python programming is no joke!"
z=y.count("p")
print(z)

#3. Write a Python program to count the occurrences of the word "python" in a given sentence below:
python_program="We are learning how to program in python. I find python programming fun"
z=python_program.count("python")
print(z)

#4. Write a Python function to reverses the word below:
word_to_be_reversed="reven"
reversed_word=word_to_be_reversed[::-1]
print(reversed_word)