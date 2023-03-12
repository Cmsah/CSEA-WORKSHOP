# RegEx
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# Python has a built-in package called re, which can be used to work with Regular Expressions.
import re

txt = "The rain in Spain"
# Search the string to see if it starts with "The" and ends with "Spain"
x = re.search("^The.*Spain$", txt)
print(x)
# Read metacharcters ,sets and special sequences from w3 schools
# https://www.w3schools.com/python/python_regex.asp

# RegEx function 
