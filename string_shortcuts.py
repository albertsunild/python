print('He said, "I want to eat an apple".')
print("He said, \"I want to eat apple\".")

name = "Bunny"

for letter in name:
    print(letter)

# stripping the string
print(name[0:])
print(name[:])
print(name[-2:-4])
print(f" There are {len(name)} characters in name variable")

## Strings are immuntables
a = "!!! Bunny !!!! Akanksh !!!"
print(len(a)) # prints the length of a
print(a.upper()) # converts the string a all to upper case
print(a.lower()) # converts the string a all to lower case
print(a.rstrip("!")) # removes the "!" at the end and not at the begining
print(a.replace("Bunny", "Avyaan")) # replaces "Harry" with "John"
print(a.split(" ")) # splits the string with the space and converts into list
print(a.center(50)) # adds addition 50 spaces before printing the string
print(a.capitalize()) #first letter would be captilise. Ex: "harry" would be converted to "Harry" 
print(a.count("Akanksh")) # counts the occurance of letter within the string
print(a.endswith("!!!")) #checks if the string ends with given conditon and returns a Boolean value
print(a.endswith("!!!", 4, 5)) #checks if the string ends with given conditon and returns a Boolean value against the given string subset


str1 = "Hello, how are you, and what are you doing these days?"
print(str1.find("are")) #finds the letter/word in the string
print(str1.index("are")) #use index to raise "ValueError: substring is not found"

str2 = "My age is just 18"
print(str2.isalnum()) # returns True if the entire string contains of A-Z, a-z, 0-9
print(str2.isalpha()) # returns True if the entire string only contains A-Z, a-z

print(str2.islower()) # checks if the string is lower or not
print(str2.isprintable()) # checks if there are any character which are not printable

print(str2.isspace()) # checks if there are any space with the variable
print(str2.istitle()) # checks if the variable is a title or not Ex: The Expandables

print(str2.startswith("My")) # checks if the string starts with character and returns Boolean
print(str2.swapcase()) # returns the string with case swaping Ex: My name = mY NAME
