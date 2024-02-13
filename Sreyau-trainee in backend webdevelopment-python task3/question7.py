# 7.Write a Python program to find palindromes in a given list of strings using Lambda.


strings = ["malayalam", "beinex", "radar", "django", "madam"]
palindrome = lambda s: s == s[::-1]

print("Palindromes in the list strings:")
for string in strings:
    if palindrome(string):
        print(string)
