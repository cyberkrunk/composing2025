# pseg is an ordered list of pitches, in pitch space
pseg = [64, 62, 60, 62, 64, 64, 64]
print(f"pseg: {pseg}")

# two ways to do transposition
transpose_interval = 4

# old fashioned way using map and a lambda function
pseg_transposed_map = list(map((lambda p: p + transpose_interval), pseg))
print(f"pseg_transposed_map: {pseg_transposed_map}")

# more current way using a list comprehension
pseg_transposed_lc = [p + transpose_interval for p in pseg]
print(f"pseg_transposed_lc: {pseg_transposed_lc}")
