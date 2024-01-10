# Task 1
"""
Write a Python program to detect the number of local variables declared in a function.
"""

def example_function():
    a = 10
    b = "Hello"
    c = [1, 2, 3]
    d = {'key': 'value'}

    local_variables = locals()
    return local_variables


result = example_function()
print(f"Number of local variables: {len(result)}")

print()
print("-" * 25)
print()

#Task 2
"""
Write a Python program to access a function inside a function
(Tips: use function, which returns another function)
"""


def outer_func(who):
    def inner_funk():
        print(f"Hello, {who}")
    inner_funk()


returned_func = outer_func("Katarina")


print()
print("-" * 25)
print()


#Task 3
"""
Write a function called "choose_func" which takes a list of nums and 2 callback functions.
If all nums inside the list are positive, execute the first function on that list and return the result of it.
Otherwise, return the result of the second one
"""

 

def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)



 

# Assertions

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

 

def square_nums(nums):

    return [num ** 2 for num in nums]

 

def remove_negatives(nums):

    return [num for num in nums if num > 0]

 

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

