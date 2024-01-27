#Task 4
"""
Custom exception

Create your custom exception named 'CustomException', you can inherit from base Exception class, but extend its functionality to log every error message to a file named 'logs.txt'.
Tips: Use __init__ method to extend functionality for saving messages to file

class CustomException(Exception):

def __init__(self, msg):
"""

class CustomException(Exception):

    def __init__(self, msg):
        super().__init__(msg)

        with open('logs.txt', 'a') as log_file:
           log_file.write(f"{msg}\n")

try:
    raise CustomException("I am a mistake")
except CustomException as e:
    print(f"An error occurred: {e}")


with open('logs.txt', 'r') as log_file:
    file = log_file.read()
    print(file)
