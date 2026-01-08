from classico import *

pseg = Pseg([60, 64, 67, 63, 64, 62, 60])

print(f"Here are some attributes:")
print(f"The size of the pseg is: {pseg.size}")
print(f"The original pseg: {pseg()}")
print(f"The interval list is: {pseg.intervals}")
print(f"The range is from {pseg.range[0]} to {pseg.range[1]}")
print(f"The ambitus is: {pseg.ambitus}")
print(f"The pcseg is: {pseg.pcseg}")
print(f"The pcset is: {pseg.pcset}")
print(f"The cardinality of its pcset is: {pseg.cardinality}")
print()

print(f"Here are some methods:")
print(f"Transposed, it is: {pseg.transpose(8)}")
print(f"But the original is still: {pseg.pitches}")
print(f"Inverted, it is: {pseg.invert()}")
print(f"But the original is still: {pseg.pitches}")
print(f"Inverted and transposed it is: {pseg.tni(8)}")
print()

print("Here are some order methods")
print(f"The retrograde of the pseg: {pseg.retrograde()}")
print()

print(f"Left rotations")
for i in range(pseg.size):
    print(f"Rotation {i * -1}: {pseg.rot(i * -1)}")
print()

print(f"Right rotations")
for i in range(pseg.size):
    print(f"Rotation {i}: {pseg.rot(i)}")
print()

print(f"Some Scrambles!")
for i in range(10):
    print(f"{pseg.scramble()}")
