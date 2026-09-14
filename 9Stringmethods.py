
c= " moulali Shaik !!!"
print(c.upper()) # converts to uppercase
print(c.lower()) # converts to lowercase
print(c.rstrip('!')) #removes the trailing characters from the right side of the string
print(c.replace('shaik', 'sher'))
print(c.split(' '))
print(c.capitalize())
w="welcome to python programming\n"
print(len(w))
print(w.center(50))
print(w.count('o'))
print(w.startswith('g'))
print(w.endswith('py',2,13))
print(w.find('to'))
print(w.index('pro'))
print(w.isalnum()) #true - only contains A-Z, a-z, 0-9
print(w.isalpha()) #true - only contains A-Z, a-z
print(w.isdigit()) #true - only contains 0-9
print(w.islower()) #true - only contains a-z
print(w.isupper()) #true - only contains A-Z
print(w.isprintable()) #true - only contains printable characters "\n isnt printable"
print(w.isspace()) #true - only contains whitespace characters
print(w.istitle()) #true - only contains titlecase characters
print(w.title())
print(w.swapcase()) #lowercase to uppercase and vice versa