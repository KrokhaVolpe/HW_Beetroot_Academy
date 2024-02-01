#Task_3
"""
Fraction

Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною перевіркою й обробкою помилок.
Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction

 class Fraction:
    pass

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)
"""

 class Fraction:
     def __init__(self, numerator, denomirator):
         if denomirator == 0:
             raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denomirator = denomirator
