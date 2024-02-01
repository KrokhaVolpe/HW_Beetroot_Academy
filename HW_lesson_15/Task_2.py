#Task 2
"""
Doggy age
Create a class Dog with class attribute 'age_factor' equals to 7. Make __init__() which takes values for a dog’s age.
Then create a method `human_age` which returns the dog’s age in human equivalent.
"""



class Dog:

    def __init__(self, dog_age):
        self.dog_age = dog_age
        self.age_factor = 7

    def human_age(self):
        return self.dog_age * self.age_factor

    def read_age(self):
        print(f"Dog age in human equivalent: {self.human_age()} years")

        
dog1 = Dog(3)
dog2 = Dog(5)
dog3 = Dog(1)

dog1.read_age()
dog2.read_age() 
dog3.read_age()

