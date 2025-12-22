from collections import deque

A = [0, 1, 5, 6, 8]
B = [0, 2, 3, 6, 7, 9]
C = [0, 1, 4, 5, 7, 9]
D = [0, 1, 2, 5, 6, 7, 9]
E = [0, 1, 3, 4, 5, 7, 8, 10]

for pcs in [A, B, C, D, E]:
    print(f"The original set is {pcs}")
    pcs.sort()
    print(f"The sorted set is {pcs}")
    d = deque(pcs)
    for r in range(len(pcs)):
        if r == 0:
            d.rotate(0)
        else:
            d.rotate(1)
        l = list(d)
        int_list = []
        for pc in range(len(l)-1):
            pc += 1
            if l[0] < l[pc]:
                int_list.append(l[pc] - l[0])
            else:
                int_list.append(l[pc] + 12 - l[0])
        print(f"Rotation {r}: {l}, {int_list}")
    print('---')
