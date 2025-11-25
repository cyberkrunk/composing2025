from music21 import *

my_scale = scale.MajorScale('C')

print(my_scale.pitches)

print(my_scale)

run = my_scale.getPitches('C4', 'C6')

print(run)

for p in my_scale.getPitches('C4', 'C6'):
    print(p.simplifyEnharmonic(inPlace=False, mostCommon=True))

# my_new_scale = scale.Scale()

# my_scale.show('text')
