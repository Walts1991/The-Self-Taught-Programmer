#When functions require a specific data type it is good practice to leave a comment at the top called a docstring
#Docstrings explain what a fucntion does and what data type each parameter needs

#http://tinyurl.com/zhahdcg

def add(x,y):
    """
    Returns x + y.
    :param x: int
    :param y: int
    :return: int sum of x + y.
    """
    return x + y

print(add(5,3))

#First line explains what the function does
#Rest of the lines list the function's parameters and their types