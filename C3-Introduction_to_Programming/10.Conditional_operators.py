#if, elif and else are used in conditional statements

#pseudocode to clarify how this works

#if (expression) then:
    #(code_area1) #if first statement is true, code in area 1 is executed)
#else:
    #(code_area2) #if first statement is false, code in area 2 is executed)
    
#http://tinyurl.com/htvy6g3 - If/Else Statement - If True

home = "America"
if home == "America":
    print("Hello America!")
else:
    print("Hello World!")

#http://tinyurl.com/jytyg5x If/Else Statement - If False

home = "Canada"
if home == "America":
    print("Hello America!")
else:
    print("Hello World!")
    
#http://tinyurl.com/jyg7dd2 - If only Statement - True

home = "America"
if home == "America":
    print("Hello America!")

#http://tinyurl.com/z24ckye - Multiple If Statements

x = 2
if x == 2:
    print("The number is 2.")
if x % 2 == 0:
    print("The number is even.")
if x % 2 != 0:
    print("The number is odd.")

#http://tinyurl.com/zrodgne - Nested If Statements

x = 10
y = 11

if x == 10:
    if y == 11:
        print(x + y)
        
# In the above example, x + y will only print if the expressions in both if statements are true
# Else statements can only be used a tthe end of an if-else statement and cannot be used on their own
# Elif (Else if) can be ussed to to make additional decisions
# If statements are evaluated first, followed by elif statements if first statement is false
# Only when a true statement is evaluated, the relevant code is executed
# If no statements are true, the else statement is executed

#http://tinyurl.com/jpr265j - If/Elif/Else Statement - Elif is True

home = "Thailand"
if home == "Japan":
    print("Hello Japan!")
elif home == "Thailand":
    print("Hello Thailand!")
elif home == "India":
    print("Hello India!")
elif home == "China":
    print("Hello China!")
else:
    print("Hello World!")

#http://tinyurl.com/zdvuuhs - If/Elif/Else Statement - Elif is False

home = "Mars"
if home == "America":
    print("Hello America!")
elif home == "Canada":
    print("Hello Canada!")
elif home == "Thailand":
    print("Hello Thailand!")
elif home == "Mexico":
    print("Hello Mexico!")
else:
    print("Hello World!")
    
#http://tiny.url.com/hzyxgf4 - Multiple If/Elif Statements

x = 100
if x == 10:
    print("10!")
elif x == 20:
    print("20!")
else:
    print("I don't know!")

if x == 100:
    print("x is 100!")

if x % 2 == 0:
    print("x is even!")
else:
    print("x is odd!")
