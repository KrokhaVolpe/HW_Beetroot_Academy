#Task 1
"""
Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except state­ment to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
"""

def oops():
    raise IndexError("This is an IndexError")

def catch_error():
    try:
        oops()
    except IndexError as e:
        print(f"Caught an IndexError: {e}")
    except KeyError as e:
        
        print(f"Caught a KeyError: {e}")
    else:
        print("No exception occurred.")

catch_error()
 
