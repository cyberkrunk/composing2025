# ---------------------------------------------------------------------
# Python code to generate ascending integer compositions, which are
# compositions in which all the summands are arranged in ascending
# order. There is only one such composition per cardinality, thus
# they are equivalent to integer partitions. This code adapted from
# Jerome Kelleher.
# 2025-09-24
# ---------------------------------------------------------------------


def accel_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[: k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[: k + 1]


print("# Ascending compositions of the integers 1-12")
print()
for i in range(1, 13):
    print(f"## Ascending compositions of {i}")
    print()
    for p in accel_asc(i):
        print(tuple(p))
    print()
