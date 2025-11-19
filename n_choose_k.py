# Sample code to calculate n choose k using SciPy.
# 2025-09-23 (rapture day)

import scipy as sp

for n in range(1, 13):
    print(f"Compositions of {n}")
    for k in range(1, n + 1):
        print(f"{k}-compositions of {n}: {int(sp.special.comb(n-1, k-1))}")
    print()
