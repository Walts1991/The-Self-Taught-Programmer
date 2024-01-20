#Calling a function means giving the function the input in needs to execute its instructions and return an output
#Each input to a function is a parameter

# Do not run - example of a mathematical function from algebra
# f(x) = x * 2

#f defines the function that takes the parameter (x)
#= function definition that uses the parameter to make a calculation and return the result (output)

#[function_name]([parameters_separated_by_commas])

#Syntax for defining a function is shown below

#def [function_name]([parameters]):
     #[function_definition]

#Above example

def f(x):
    return x * 2

#Keyword def tells Python you are defining a function
#Keyword return defines the value a function outputs 

#Function names follow the same rules as variable names
#Functions start with a lowercase letter or an underscore, followed by letters, digits and/or underscores 
#They can also be composed of multiple words separated by underscores
#Function names should describe what the function does

#You can use the syntax [function_name]([parameters_separated_by_commas]) to call a previously defined function

f(2) #Generates output
print(f(2)) #Prints output

#Can save function's output as a variable and pass to the print function

result = f(2)
print(result)

#http://tinyurl.com/znqp8fk

def f(x):
    return x + 1

z = f(4)

if z == 5:
    print("z is 5")
else:
    print("z is not 5")

#A function can have one parameter, multiple parameters or no parameters
#To define a function that does not require parameters, leave the parenthesis empty i.e. ()

#http://tinyurl.com/htk7tr6

def f():
    return 1 + 1

result = f()
print(result)

#For functions to accept multiple parameters, these must be separated using commas within the parentheses

#http://tinyurl.com/gwmkft7

def f(x,y,z):
    return x + y + z

result = f(1,2,3)
print(result)

#A function does not have to include a return statement
#If a function does not include a return statment, it returns none

#http://tinyurl.com/j8qyqov

def f():
    z = 1 + 1
    
result = f()
print(result)
