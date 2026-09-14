# if-else conditionla statements in python
'''if else statements are used to execute a block of code if a condition is true
 and another block of code if the condition is false.'''

#conditional operators in python
# ==, !=, >, <, >=, <=

A=int(input("enter a number: ")) #input function is used to take input from the user and int function is used to convert the input into integer
n=("entered number is:",A)
print(A==18) #checks if the age is equal to 18
print(A!=18) #checks if the age is not equal to 18
print(A>18) #checks if the age is greater than 18
print(A<18) #checks if the age is less than 18
print(A>=18) #checks if the age is greater than or equal to 18
print(A<=18) #checks if the age is less than or equal to 18

e=int(input("enter your age: ")) #input function is used to take input from the user and int function is used to convert the input into integer
age=("your age is:",e)
if (e>=18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

#elif statement is used to check multiple conditions in python
budget=5000
watchprice = int(input("enter the price of the watch: "))
if budget-watchprice==2000:
    print("alexa add it to cart")
elif budget-watchprice<=1500:
    print("alexa dont add it to cart")
elif budget-watchprice<500:
    print("no need to buy a watch")
else:
    print("alexa check for other options")
