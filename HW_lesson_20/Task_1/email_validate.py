#Task 1
"""
Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email, passed to the constructor.
The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.
"""

import re

class Email:

    PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    def __init__(self, address):
        self.address = Email.validate(address)
        if Email.validate(address):
            self.address = address

        else:
            raise ValueError(f"Invalid email address: {address}")

                    
    @classmethod    
    def validate(cls, address):
        return bool(re.match(cls.PATTERN, address))

