# This is sample code to read in the fibonacci.json file and load it
# into a python dictionary.
# 2025-09-22

import json

with open("fibonacci.json", "r") as f:
    fibonacci_dict = json.load(f)

# Need to convert the keys back into integers (json stores them as
# strings). This method uses python dictionary comprehension.

fibonacci_dict = {int(k): v for k, v in fibonacci_dict.items()}

print(fibonacci_dict)

print(fibonacci_dict[12])
