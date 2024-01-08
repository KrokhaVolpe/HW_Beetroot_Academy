def calculate_squared_division():
        
        try:
            number_a = float(input("Enter first number: "))
            number_b = float(input("Enter second number: "))
            
            result = (number_a ** 2) / number_b
            print(result)
            
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError:
            print("You can't divide by zero!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

result = calculate_squared_division()

