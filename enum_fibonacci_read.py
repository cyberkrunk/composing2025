# ---------------------------------------------------------------------
# This is sample code to read in the fibonacci.json file and load it
# into a python dictionary.
# 2025-09-22
# ---------------------------------------------------------------------

import json

with open("output/fibonacci.json", "r") as file:
    fibonacci_dict = json.load(file)

# Convert the keys back into integers (json stores them as
# strings). This method uses Python dictionary comprehension.

fibonacci_dict = {int(key): value for key, value in fibonacci_dict.items()}

print(f"fibonacci_dict: {fibonacci_dict}\n")
print(f"Just the values as a list: {[value for key, value in fibonacci_dict.items()]}\n")

print(f"Not sure what this is: {fibonacci_dict[12]+fibonacci_dict[10]}")
