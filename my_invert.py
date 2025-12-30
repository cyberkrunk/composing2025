# ---------------------------------------------------------------------
# Two different ways to invert a pseg
# 2025-12-29
# ---------------------------------------------------------------------

# 1: Invert using an interval list
pseg = [48, 49, 50, 51, 52]
interval_list = []
for i in range(len(pseg)):
    interval = pseg[i] - pseg[0]
    interval_list.append(interval)
interval_list_inverted = [interval * -1
                          for interval in interval_list]
pseg_inverted = [pseg[0] + interval
                 for interval in interval_list_inverted]
print("Method 1")
print(f"pseg: {pseg}")
print(f"interval_list: {interval_list}")
print(f"interval_list_inverted: {interval_list_inverted}")
print(f"pseg_inverted: {pseg_inverted}")
print("---")

# 2: Invert using an inversion index
# and a list comprehension - one-step
pseg = [60, 61, 62, 63, 64]
inversion_index = pseg[0] * 2
pseg_inverted = [inversion_index - p
                 for p in pseg]
print("Method 2")
print(f"pseg: {pseg}")
print(f"pseg_inverted: {pseg_inverted}")