#http://tinyurl.com/zfkzqw6 - len - returns the length of an object

print(len("Monty"))

#http://tinyurl.com/h75c5cf

print(len("Python"))

#http://tinyurl.com/juzxg2z - str - converts integers to strings

print(str(100))

#http://tinyurl.com/j42qhkf - int - converts object to integer

print(int("1"))

#http://tinyurl.com/hnk8gh2 - float - converts objects to to floating point objects

print(float(100))

#str functions can accepts most objects as a parameter
#int function can only accept a string with a number in it or a floating point object
#float function can only take a string with a number in it or an integer object

#http://tinyurl.com/jcchmlx

print(int("110"))
print(int(20.54))
print(float("16.4"))
print(float(99))

#Python will raise an exception if the parameter cannot be converted

#http://tinyurl.com/zseo21s - Exception error

#print(int("Prince"))

#The input function collects information from the person using the program

#http://tinyurl.com/zynprpg - input function

age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("You are young!")
else:
    print("You are old!")

#The input function takes a string as a parameter
#Inputs can be saved into variables
#The int function can be used to change the string variable to an integer for comparison
#If-else statement can then be used to determine message to be printed to user depending on input