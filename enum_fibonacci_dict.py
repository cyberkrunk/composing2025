# ---------------------------------------------------------------------
# This is python code to calculate the first 40 Fibonacci numbers in a
# python dictionary, then write that dictionary to a json file for use
# in other programs. 40 was chosen because it is the next greater
# Fibonacci number than the number of milliseconds in a day (86400000),
# and I can't think of why I need a Fibonacci number greater than that
# for composing.
# 2025-09-22
# ---------------------------------------------------------------------

import json

fibonacci_dict = {0: 0, 1: 1}
for i in range(2, 41):
    fibonacci_dict[i] = fibonacci_dict[i - 1] + fibonacci_dict[i - 2]

with open("fibonacci.json", "w") as f:
    json.dump(fibonacci_dict, f)
