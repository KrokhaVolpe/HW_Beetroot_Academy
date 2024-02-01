#Task 1
"""
Method overloading.

Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, and make their own implementation of the method
talk be different. For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method on input parameter.
"""

class Animal:
    def __init__(self, name, age, favorite_snack):
        self.name = name
        self.age = age
        self.favorite_snack = favorite_snack

    def talk(self):
        pass

    def info(self):
        return f"My name is {self.name}. I am {self.age} years old."

    def describe_favorite_snack(self):
        return f"I love {self.favorite_snack}"


class Cat(Animal):
    def __init__(self, name, age, favorite_snack):
        super().__init__(name, age, favorite_snack)
        
    def talk(self):
        return "Meow!"



class Dog(Animal):
    def __init__(self, name, age, favorite_snack, trick):
        super().__init__(name, age, favorite_snack)
        self.trick = trick

    def talk(self):
        return "Woof woof!"

    def describe_trick(self):
        return f"I know the team: {self.trick}"


def perform_talk(animal_instance):
    print(f"{animal_instance.talk()}\n{animal_instance.info()}")


cat1 = Cat('Alice', 2, 'meat')
perform_talk(cat1)
print(cat1.describe_favorite_snack())
print()

dog1 = Dog('Jack', 1, 'meat', 'sit, voice')
perform_talk(dog1)
print(dog1.describe_favorite_snack())
print(dog1.describe_trick())

