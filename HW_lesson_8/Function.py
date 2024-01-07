#Task 1
"""
A simple function.
Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
The function should then print "My favorite movie is named {name}"
"""

def favorite_movie(movie):
    print(f"My favorite movie is named {movie}")


user_movie = input("Enter your favorite movie: ")
favorite_movie(user_movie)
print("-" * 30)



#Task 2
"""
Creating a dictionary.
Create a function called make_country, which takes in a country’s name and capital as parameters.
Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
Make the function print out the values of the dictionary to make sure that it works as intended.
"""


def make_country():
    country = input("Enter the country name: ")
    capital = input("Enter the capital of the country: ")
    country_dict = {'name': country, 'capital': capital}
    print(country_dict)
    
make_country()


#Task 3
"""
A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be '+', '-' or '*')
and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter.
For example:
the call make_operation('+', 7, 7, 2) should return 16
the call make_operation('-', 5, 5, -10, -20) should return 30
the call make_operation('*', 7, 6) should return 42
"""

def make_operation(operator, *args):
    result = 0

    if operator == '+':
        result = sum(args)
    elif operator == '-':
        result = args[0] - sum(args[1:])
    elif operator == '*':
        result = 1
        for num in args:
            result *= num

    return result


result_addition = make_operation('+', 7, 7, 2)
result_subtraction = make_operation('-', 5, 5, -10, -20)
result_multiplication = make_operation('*', 7, 6)

print(f"Result of addition: {result_addition}")
print(f"Result of subtraction: {result_subtraction}")
print(f"Result of multiplication: {result_multiplication}")


