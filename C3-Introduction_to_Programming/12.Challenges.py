# 1. Print three different strings

print("Hello World")
print("My name is Guy")
print("I am 32 years old")

# 2. Write a proram that prints a message if a variable is less than 10,
# and a different message if the variable is greater than or equal to 10.

x = 8
if x < 10:
    print("x is less than 10")
else:
    print("x is greater than or equal to 10")

# 3. Write aprogram that prints a message if a variable is less than or equal to 10,
# another message if the variable is greater than 10 but less than or equal to 25, 
# and another message if the variable is greater than 25.

x = 16
if x <= 10:
    print("x is less than or equal to 10")
elif x <= 25:
    print("x is greater than 10 but less that or equal to 25")
else:
    print("x is greater than 25")

# 4. Create a program that divides two variables and prints the remainder

x = 10
y = 6

print(x % y)

# 5. Create a program that takes two variables, divides them, and prints the quotient

print(x // y)

# 6. Write a program with a variable age assigned to an integer that prints different strings depending on what integer the age is.

age = 32

if age < 18:
    print("You are a child")
elif age >= 65:
    print("You are elderly")
else:
    print("You are an adult")
    
#Proposed solution below:

age = 64
retirement = age - 65

if retirement < 10:
    print("You get to retire soon.")
else:
    print("You have a long time until you can retire!")


# Solutions: http://tinyurl.com/zx7o2v9