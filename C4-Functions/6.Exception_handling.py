#User input functions can create errors if not properly controlled

#http://tinyurl.com/jcg5qwp

a = input("type a number: ")
b = input("type another: ")
a = int(a)
b = int(b)
print(a / b)

#http://tinyurl.com/ztpcjs4 - Above calculation would not work if user input a zero as the 2nd number i.e. ZeroDivisionError

a = input("type a number: ")
b = input("type another: ")
a = int(a)
b = int(b)
print(a / b)

#One way to resolve this is to use exception handling which allows tests for error conditions
#Keywords try and except are used
#Instead of raising an exception a message could be displayed to advise user of error e.g. not enter zero

#Each exception in Python is an object
#List of built-in exceptions can be found here - http://www.tutorialspoint.com/python/standard_exceptions.htm

#Try clause contains the error that could occur
#Except clause contains code that will only excute if the exception in try clause occurs

#http://tinyurl.com/j2scn4f - Exception handling example

a = input("type a number: ")
b = input("type another: ")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero")

#If the user does not enter 0 for b, the code in the try block executes 
#If the user does enters 0 for b, the code in the except block executes 

#Program will also break if user enters a string that python cannot convert to an integer
#This can be resolved by adding another exception error for a ValueError exception if there is an invalid data type
#This is done by adding parenthesis and separating the exceptions with a comma

try:
    a = input("type a number: ")
    b = input("type another: ")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError,ValueError):
    print("Invalid input.")

#Don't use variables defined in a try statement within an except statement as the exception could occur before the variable is defined
#Exception will get raise inside of your except statement when it is used

#http://tinyurl.com/hockur5

try:
    10 / 0
    c = "I will never be defined"
except ZeroDivisionError:
    print(c)
    