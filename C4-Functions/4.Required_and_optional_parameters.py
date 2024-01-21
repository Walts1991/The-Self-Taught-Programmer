#There are two types of parameters a function can accept
#Required parameters - All parameters must be passed otherwise Python will raise an exception
#Optional parameters - If optional paramaters are not passed in, the function will use its default value instead
#Optional parameters are defined with the syntax: [function_name]([parameter_name]=[parameter+value])
#Like required parameters, optional parameters must be separated by commas

#http://tinyurl.com/h3ych4h - Optional parameter example

def f(x=2):
    return x**x

print(f())
print(f(4))

#First print uses the default value of 2 as no parameter is used.  Paramter of 4 is used for second print

#You can define a function that has both required and optional parameters
#All required parameters must be defined before optional parameters

def add_it(x, y=10):
    return x + y

result = add_it(2)
print(result)

def add_it(x, y=10):
    return x + y

result = add_it(2,4)
print(result)
