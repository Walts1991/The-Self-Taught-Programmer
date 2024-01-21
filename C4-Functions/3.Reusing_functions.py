#Functions are not only used to compute and return values
#Functions can encapsulate functionality you want to reuse

#http://tinyurl.com/zhy8y4m

def even_odd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")
        
even_odd(2)
even_odd(3)

#Functions allow you to write less code as they can be reused:

#http://tinyurl.com/jk8lugl - Code without reusing functions

n = input("Type a number:")
n = int(n)

if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")


n = input("Type a number:")
n = int(n)

if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")


n = input("Type a number:")
n = int(n)

if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")

#The code can be made shorter by defining a function and calling it multiple times

#http://tinyurl.com/zzn22mz

def even_odd():
    n = input("Type a number:")
    n = int(n)
    if n % 2 == 0:
        print("n is even")
    else:
        print("n is odd")
        
even_odd()
even_odd()
even_odd()
