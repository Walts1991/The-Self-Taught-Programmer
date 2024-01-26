#Variables have an important property called scope
#Global variables are defined outside of a function or class
#Local variables are defined inside of a function or class

#Global variables can be read or written to from anywhere, including inside of a function

#http://tinyurl.comhgvnj4p - Global scope

x = 1
y = 2
z = 3

def f():
    print(x)
    print(y)
    print(z)
    
f()

#Local variables can only be read or written from inside the function
#Local variables cannot be access from outside of the function they were defined in

#http://tinryurl.com/znka93k - Local Scope - NameError: "x" is not defined
#
"""
def f():
    x = 1
    y = 2
    z = 3

print(x)
print(y)
print(z)
"""

#http://tinyurl.com/z2k3jds - Local Scope - Variables defined within function

def f():
    x = 1
    y = 2
    z = 3
    print(x)
    print(y)
    print(z)

f()

#http://tinyurl.com/zn8zjmr - Variable not defined - NameError: "x" is not defined

if x > 100:
    print("x is > 100")

#http://tinyurl.com/zclmda7 - Global variables can be written to from a local function by using the global keyword

x = 100

def f():
    global x
    x += 1
    print(x)
    
f()

