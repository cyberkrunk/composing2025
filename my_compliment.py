from music21 import *



my_chord = chord.Chord(["C4", "E-4", "B4"])
A = [p.pitchClass for p in my_chord.pitches]  # The chord.
U = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # The aggregate.
C = [pc for pc in U if pc not in A]  # The complement.

print(f"A = {A}")
print(f"U = {U}")
print(f"C = {C}")


my_chord = chord.Chord("C4 E-4 C-4")
print(my_chord)
for p in my_chord:
    print(p.pitch)
    print(p.pitch.pitchClass)
