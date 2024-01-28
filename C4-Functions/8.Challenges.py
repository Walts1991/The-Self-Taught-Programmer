#1. Write a function that takes a number as an input and returns that number squared

def nsquared(x):
    """
    returns an int of x squared.
    :param x: int.
    :return: int of x squared
    """
    return x ** 2
    
print(nsquared(4))

#2. Create a function that accepts a string as a parameter and prints it.

def print_string(string):
    """
    Prints a string which is entered by user
    :param string: str
    """
    print(string)
    
print_string("Testing: 1, 2, 3")

#3. Write a function that takes three required parameters and two optional parameters.

def function(a,b,c,x=10,z=5):
    """
    Returns the result of 2 optional parameters multipled by the addition of 3 required parameters
    x * z * c + b + a
    :param a: int
    :param b: int
    :param c: int
    :param x: int
    :param z: int
    :returns: int of function
    """
    return a + b + c * x * z

result = function(8, 4, 2)
print(result)

#4.Write a program with two functions.
#The first function should take an integer as a parameter and return the result of the integer divided by 2.
#The second function should take an integer as a parameter and return the result of the integer multiplied by 4.
#Call the first function, save the result as a variable, and pass it as a parameter to the second function

def div(i):
    """
    returns i divided by 2
    :param i: int.
    :return: int of i divided by 2
    """
    return i / 2

def mult(i):
    """
    returns i multiplied by 4
    :param i: int.
    :return: int of i multiplied by 4
    """
    return i * 4

d = div(6)
m = mult(d)

print(d)
print(m)

#5. Write a function that converts a string to a float and returns the result.
#Use exception handling to catch the exception that could occur.  

def convert(string):
    """ 
    returns the string as a float unless the string cannot be converted to a float
    :param string: str
    :return: float of string
    :except: error message stating unable to convert to float
    """
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float")

c = convert("32")
print(c)

#6.Add a docstring to all of the functions you wrote in challenges 1-5.

#Docstrings included in above answers for challenges 1-5

#Solutions: http://tinyurl.com/hkzgqrv