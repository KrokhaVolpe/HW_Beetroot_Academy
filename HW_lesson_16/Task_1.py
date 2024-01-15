#Task 1
"""
School

Make a class structure in python representing people at school. Make a base class called Person, a class called Student, and another one called Teacher.
Try to find as many methods and attributes as you can which belong to different classes, and keep in mind which are common and which are not.
For example, the name should be a Person attribute, while salary should only be available to the teacher.
"""


class  Person():
    def __init__(self, full_name, age, address):
        self.last_name = full_name
        self.age = age
        self.address = address
        self.school_number = 205

    def print_info(self):
         print(f"Hello, my name is {self.last_name}, I am {self.age} years old.")

    
class Student(Person):
    def __init__(self, full_name, age, address, number_items, average_score):
        super().__init__(full_name, age, address)
        self.number_items = number_items
        self.average_score = average_score

    def print_items_score(self):
        print(f"Average score: {self.average_score}")
    

class Teacher(Person):
    def __init__(self, full_name, age, address, salary, number_hours):
        super().__init__(full_name, age, address)
        self.salary = salary
        self.number_hours = number_hours


    def get_salary_hours(self):
        print(f"Hours worked {self.number_hours}. Accrued {self.salary} ")
    

    

student1 = Student("Alice Smith", 18, "address1", "5", "100")
student1.print_info()
student1.print_items_score()


teacher1 = Teacher("Mr. Johnson", 40, "address2", "11502", 50)
teacher1.print_info()
teacher1.get_salary_hours()
