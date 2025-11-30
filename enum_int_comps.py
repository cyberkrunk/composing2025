# ---------------------------------------------------------------------
# This is python code to generate all strong compositions of the
# integers 1-12. Printing is formatted to be used in a .md file.
# 2025-09-22
# ---------------------------------------------------------------------

import scipy as sp


def strong_compositions(n, k, current_composition=None):
    if current_composition is None:
        current_composition = []
    if k == 0:
        if n == 0:
            yield current_composition
        return
    for i in range(1, n - k + 2):
        yield from strong_compositions(n - i, k - 1, current_composition + [i])


print("# Strong compositions of the integers 1-12")
print()
for n in range(1, 13):
    print(f"## Compositions of {n}")
    print()
    for k in range(1, n + 1):
        print(f"### {k}-compositions of {n}: {int(sp.special.comb(n-1, k-1))}")
        print()
        for comp in strong_compositions(n, k):
            print(tuple(comp), end=", ")
        print(" ")
        print()
