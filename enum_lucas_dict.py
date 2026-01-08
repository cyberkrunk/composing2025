# ---------------------------------------------------------------------
# This is python code to calculate the first 38 Lucas numbers in a
# python dictionary, then write that dictionary to a json file for use
# in other programs. 38 was chosen because it is the next greater lucas
# number than the number of milliseconds in a day (86400000), and I
# can't think of why I need a lucas number greater than that for
# composing.
# 2025-09-22
# ---------------------------------------------------------------------

import json

lucas_dict = {0: 2, 1: 1}
for i in range(2, 39):
    lucas_dict[i] = lucas_dict[i - 1] + lucas_dict[i - 2]

with open("output/lucas.json", "w") as f:
    json.dump(lucas_dict, f)
