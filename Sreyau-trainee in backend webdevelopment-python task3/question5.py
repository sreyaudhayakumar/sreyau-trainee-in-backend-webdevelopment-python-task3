# 5.Write a Python program to check whether a given string is a number or not using Lambda.

is_number = lambda s: s.replace(".", "", 1).isdigit()

input_string = input("Enter a string: ")

if is_number(input_string):
    print("The string ", input_string, " is a number.")
else:
    print("The string ", input_string, " is not a number.")
