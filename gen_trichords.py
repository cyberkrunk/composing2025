# ---------------------------------------------------------------------
# This code generates trichords by incrementing the outer voice while
# keeping the inner voice constant. The chord stream that it generates
# is not symmetrical. The _sym version of this code generates a
# symmetrical chord stream.
#
# 2025-12-22
# ---------------------------------------------------------------------

import copy
from music21 import chord

start_chord = [0, 1, 2]
chord_stream = []
current_chord = []
counter = 0

while start_chord[2] < 12:
    current_chord = copy.deepcopy(start_chord)
    counter += 1
    print(
        f"{counter}: start_chord = {start_chord}, i = 0, current_chord = {current_chord}"
    )
    chord_stream.append(copy.deepcopy(current_chord))
    for i in range(start_chord[2] + 1, 12):
        current_chord[2] = i
        counter += 1
        print(
            f"{counter}: start_chord = {start_chord}, i = {i}, current_chord = {current_chord}"
        )
        chord_stream.append(copy.deepcopy(current_chord))
    start_chord[1] += 1
    start_chord[2] += 1

for my_chord in chord_stream:
    m21_chord = chord.Chord(my_chord)
    print(f"{my_chord} {m21_chord.forteClassTn}")

print(f"There are {len(chord_stream)} chords.")
