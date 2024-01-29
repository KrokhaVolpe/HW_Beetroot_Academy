#Task 1
"""
Write a decorator that prints a function with arguments passed to it.

NOTE! It should print the function, not the result of its execution!

For example:

 "add called with 4, 5"

```

def logger(func):

    pass

 

@logger

def add(x, y):

    return x + y

 

@logger

def square_all(*args):

    return [arg ** 2 for arg in args]

"""

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} called with {args}, {kwargs}")
        return func(*args, **kwargs)

    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5)
square_all(1, 2, 3, 4)


#Task 2
"""
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

'''

def stop_words(words: list):

    pass

 

@stop_words(['pepsi', 'BMW'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"

 

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
"""

def stop_words(stop_words_list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for stop_word in stop_words_list:
                result = result.replace(stop_word, '*')
            return result
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"



#Task 3
"""
Write a decorator "arg_rules" that validates arguments passed to the function.

A decorator should take 3 arguments:

max_length: 15

type_: str

contains: [] - list of symbols that an argument should contain

If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.

```

def arg_rules(type_: type, max_length: int, contains: list):

    pass

 

@arg_rules(type_=str, max_length=15, contains=['05', '@'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"

 

assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('05years') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
"""


def arg_rules(type_, max_length, contains):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                
                if type(arg) is not type_:
                    print(f"Error: {func.__name__} called with {args}, {kwargs}. Argument type should be {type_.__name__}")
                    return False

               
                if max_length is not None and len(str(arg)) > max_length:
                    print(f"Error: {func.__name__} called with {args}, {kwargs}. Argument length exceeds {max_length}")
                    return False

               
                if contains is not None and not all(symbol in str(arg) for symbol in contains):
                    print(f"Error: {func.__name__} called with {args}, {kwargs}. Argument should contain symbols {contains}")
                    return False

            return func(*args, **kwargs)

        return wrapper

    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


create_slogan(123)  
create_slogan('johndoe05@gmail.com')  
create_slogan('05years') 
create_slogan('S@SH05')  



