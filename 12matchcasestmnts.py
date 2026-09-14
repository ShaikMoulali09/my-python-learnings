x=int(input("enter x value:"))
match x: #match statement compares a given variable's value to different shapes also referred to as patterns
    case 0: #pattern 1
        print("x is zero")
    case 9: #pattern 2
        print("x is nine")
    case _ if x!=90: # if x matches with 90 executes if it isn't then 80 case matches like 90 != 90 goes to 80
        print(x," is not 90")
    case _ if x!=80:
        print(x," is not 80")
    case _:
        print("x")