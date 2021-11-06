import time
"""
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object
without modifying its structure. Decorators are usually called before the definition of a function you want
to decorate.
In this tutorial, we'll show the reader how they can use decorators in their Python functions.

"""
## Assigning Functions to Variables
def plus_one(number):
    return number + 1

add_one = plus_one
# assign the function to a variable and use this variable to call the function.
print(add_one(5))


# Defining Functions Inside other Functions
def plus_one(function):
    def add_one(function):
        return function + 1

    result = add_one(function)
    return result

print(plus_one(4))

### Passing Functions as Arguments to other Functions

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

print(function_call(plus_one))

### Functions Returning other Functions

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
print(hello())

### UPPER CASE

## 1
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def say_hello():
    return "Hello world"


decorate = uppercase_decorator(say_hello)
print(decorate())


## 2

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

@uppercase_decorator
def say_hello():
    return "Hello world"

print(say_hello())


### Applying Multiple Decorators to a Single Function

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
print(say_hi())



### Accepting Arguments in Decorator Functions
"""
Sometimes we might need to define a decorator that accepts arguments. 
We achieve this by passing the arguments to the wrapper function.
 The arguments will then be passed to the function that is being decorated at call time.
"""
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Mumbai", "Delhi")

## Defining General Purpose Decorators
"""
To define a general purpose decorator that can be applied to any function we use args and **kwargs. 
args and **kwargs collect all positional and keyword arguments and stores them in the args and kwargs variables. 
args and kwargs allow us to pass as many arguments as we would like during function calls.
"""
## 1
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()

### 2
@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1,2,3)

##3
@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")

function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")




### Passing Arguments to the Decorator
"""
Now let's see how we'd pass arguments to the decorator itself. 
In order to achieve this, we define a decorator maker that accepts arguments then define a decorator inside it. 
We then define a wrapper function inside the decorator as we did earlier.
"""

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator


pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")


#### Debugging Decorators
"""
As we have noticed, decorators wrap functions. The original function name, its docstring, 
and parameter list are all hidden by the wrapper closure: For example, when we try to access 
the decorated_function_with_arguments metadata, 
we'll see the wrapper closure's metadata. This presents a challenge when debugging.
"""
print(decorated_function_with_arguments.__name__)
print(decorated_function_with_arguments.__doc__)

"""
Python provides a functools.wraps decorator,
This decorator copies the lost metadata from the undecorated function to the decorated closure
"""

import functools

def uppercase_decorator(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_decorator
def say_hi():
    "Hi Jitendra, it's decorator function"
    return 'hello there'

print(say_hi())
print(say_hi.__name__)
print(say_hi.__doc__)




def time_call(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(func.__name__ + " took " + str(end_time - start_time))
        return result
    return wrapper

@time_call
def cal_sql(n):
    lst=[]
    for i in n:
        lst.append(i*i)
    return lst

@time_call
def cal_cube(n):
    lst=[]
    for i in n:
        lst.append(i*i*i)
    return lst


value= range(100)
cal_sql(value)
cal_cube(value)


### Uses Of Decorator Function
"""
decorators in Python also ensures that your code is DRY(Don't Repeat Yourself). 
Decorators have several use cases such as:
"""
#1. Authorization in Python frameworks such as Flask and Django
#2. Logging
#3. Measuring execution time
#4. Synchronization

## Python built-in libarary
#https://wiki.python.org/moin/PythonDecoratorLibrary

