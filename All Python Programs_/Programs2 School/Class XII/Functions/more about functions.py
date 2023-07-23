----------------------------------
def f():
    global s
    print(s)
    s = "Only in spring, but London is great as well!"
    print(s)


s = "I am looking for a course in Paris!" 
f()
print(s)
We have solved our problem. There is no ambiguity left. The output of this small script looks like this:
I am looking for a course in Paris!
Only in spring, but London is great as well!
Only in spring, but London is great as well!
Local variables of functions can't be accessed from outside, when the function call has finished:
def f():
    s = "I am globally not known"
    print(s) 

f()
print(s)
Starting this script gives us the following output with an error message:
monty@python:~$ python3 ex.py 
I am globally not known
Traceback (most recent call last):
  File "ex.py", line 6, in <module>
    print(s)
NameError: name 's' is not defined
monty@python:~$ 
The following example shows a wild combination of local and global variables and function parameters:
 
def foo(x, y):
    global a
    a = 42
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print(a,b,x,y)

a, b, x, y = 1, 15, 3,4 
foo(17, 4)
print(a, b, x, y)
The output looks like this:
42 17 4 17
42 15 3 4
----------------------------------
Global Variables in Nested Functions
We will examine now what will happen, if we use the global keyword inside of nested functions. The following example shows a situation where a variable x is used in various scopes:
def f():
    x = 42
    def g():
        global x
        x = 43
    print("Before calling g: " + str(x))
    print("Calling g now:")
    g()
    print("After calling g: " + str(x))
    
f()
print("x in main: " + str(x))
This program returns the following results:
Before calling g: 42
Calling g now:
After calling g: 42
x in main: 43
----------------------------------
nonlocal
def f():
    global x
    print(x)
    
x = 3
f()
----------------------------------
def f():
    nonlocal x
    print(x)
    
x = 3
f()
The program, which we have saved as example1.py, cannot be executed anymore now. We get the following error:
 File "example1.py", line 2
    nonlocal x
SyntaxError: no binding for nonlocal 'x' found
----------------------------------
def f():
    x = 42
    def g():
        nonlocal x
        x = 43
    print("Before calling g: " + str(x))
    print("Calling g now:")
    g()
    print("After calling g: " + str(x))
    
x = 3
f()
print("x in main: " + str(x))
Calling the previous program results in the following output:
Before calling g: 42
Calling g now:
After calling g: 43
x in main: 3
----------------------------------
def f():
    #x = 42
    def g():
        nonlocal x
        x = 43
    print("Before calling g: " + str(x))
    print("Calling g now:")
    g()
    print("After calling g: " + str(x))
    
x = 3
f()
print("x in main: " + str(x))
We get the following error message:
  File "example3.py", line 4
    nonlocal x
SyntaxError: no binding for nonlocal 'x' found
------------------------

def f():
    #x = 42
    def g():
        global x
        x = 43
    print("Before calling g: " + str(x))
    print("Calling g now:")
    g()
    print("After calling g: " + str(x))
    
x = 3
f()
print("x in main: " + str(x))
This leads to the following output:
Calling g now:
The value of x after the call to g: 43
Before calling g: 3
Calling g now:
After calling g: 43
x in main: 43
