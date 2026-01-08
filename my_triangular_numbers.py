for row in range(1, 11):
    numbers = []
    for one_number in range(1, row + 1):
        numbers.append(one_number)
    print(f"{row}: {sum(numbers)} ({' '.join(map(str, numbers))})")
print()

print("$$\\begin{array}{c}")
for row in range(1, 11):
    numbers = []
    for one_number in range(1, row + 1):
        numbers.append("\\bullet")
    print(f"{'\\,\\,\\,\\,'.join(map(str, numbers))}\\\\")
print("\\end{array}$$\n")

print("$$\\begin{array}{c}")
for row in range(1, 11):
    numbers = []
    for one_number in range(1, row + 1):
        numbers.append(one_number)
    print(f"{'\\,\\,\\,\\,'.join(map(str, numbers))}\\\\")
print("\\end{array}$$")