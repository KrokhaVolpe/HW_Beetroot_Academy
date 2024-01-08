import sys


"""The sys module.
The “sys.path” list is initialized from the PYTHONPATH environment variable. Is it possible to change it from within Python?
If so, does it affect where Python looks for module files? Run some interactive tests to find it out.
"""


#I used sys.path in Python to change the path of the module search at runtime.


# Displaying current values sys.path
print("Current sys.path:", sys.path)
print("=" * 50)

# If you import the module before adding its path to sys, it may not be found

# Append the directory path, not the file path
sys.path.append(r"C:\Users\Max\OneDrive\Desktop\Katarina\HW_9_import\task_1")

# Now you can import the module
import def_make_pizza


