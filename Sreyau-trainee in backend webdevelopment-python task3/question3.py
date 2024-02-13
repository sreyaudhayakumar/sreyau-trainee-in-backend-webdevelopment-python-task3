# Write a Python program to find if a given string starts with a given character using Lambda. 

input_string = input("Enter a string: ")
input_char = input("Enter a character: ")

starts_with = lambda string, char: string[0] == char

if starts_with(input_string, input_char):
    print(input_string," starts with the character ",input_char)
else:
    print(input_string,"does not start with the character",input_char)
