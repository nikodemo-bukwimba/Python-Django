#Syntax error
while True print('Hello world')

#Exceptions
# ZeroDivisionError
n = 10 * (1/0)

#NameError
m = 4 + sparm * 3

#TypeError
p = '2' + 2

#Handling Exceptions
while True:
    try:
        x = int(input("Please enter the number: "))
        break
    except ValueError:
        print("Oops! That was not valid number. Try again...")
