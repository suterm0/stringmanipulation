# Michael Suter
# String manipulation
# 2/5/20
print("Please type words separated by commas like so 'hair, gel, shampoo.'")
string = input(">>>")
print("here is the last letter", string[-1:], "here is the first letter", string[0:1])
print("This capitalizes the first letter of every word.", string.title())
print("This makes the everything uppercase", string.upper())
print("This will return True if there are no numbers or symbols.", string.isalpha())
print("This prints every 3rd letter", string[::3])
print("This print the third letter", string[2])
print("This will turn the string entered into a list", string.split())
