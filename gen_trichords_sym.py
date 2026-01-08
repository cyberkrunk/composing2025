# ---------------------------------------------------------------------
# This code generates trichords by incrementing the outer voice, then
# keeping it constant while the inner voice increments. The chord
# stream that it generates is symmetrical.
#
# 2025-12-22
# ---------------------------------------------------------------------

import copy
from music21 import *
from classico import Pseg
# from collections import Counter
from cjcomp import pchord_int_label_latex, pchord_int_label, setup_score

my_chord = Pseg([0, 1, 2])
start_chord = my_chord.pitches
current_chord = []
chord_row = []
chord_stream = []
forte_list = []

# create the chord stream that generates the triangle
for outer_voice in range(start_chord[2], start_chord[0] + 12):
    current_chord = copy.deepcopy(start_chord)
    chord_row = []
    for inner_voice in range(start_chord[1], outer_voice):
        current_chord[1] = inner_voice
        current_chord[2] = outer_voice
        chord_row.append(copy.deepcopy(current_chord))
    chord_stream.append(copy.deepcopy(chord_row))

# print the chord stream
print(f"## The raw chord stream, a list of lists\n")
print(f"{chord_stream}\n")

# print the triangle as lists
print("## The triangle as rows of lists\n")
for index, one_row in enumerate(chord_stream):
    print(f"Row {index +1}: {', '.join(map(str, one_row))}")
print()


# print the triangle as tuples, format for md LaTeX
print("## The triangle as tuples\n")
print("$$\\begin{array}{c}")
for index, one_row in enumerate(chord_stream):
    print(
        f"{',\\,\\,\\,'.join(map(str, (tuple(one_chord) for one_chord in one_row)))}\\\\"
    )
print("\\end{array}$$\n")

# print the triangle as interval labels, format for md LaTeX
print("## The triangle as interval labels\n")
print("$$\\begin{array}{c}")
for one_row in chord_stream:
    print(
        f"{',\\,\\,\\,'.join(map(str, (pchord_int_label_latex(one_chord) for one_chord in one_row)))}\\\\[10pt]"
    )
print("\\end{array}$$\n")

# print the triangle as interval labels, format for md text
print("## The triangle as interval labels\n")
for one_row in chord_stream:
    print(
        f"{', '.join(map(str, (pchord_int_label(one_chord) for one_chord in one_row)))}"
    )
print()

# print the triangle as Forte labels, format for md LaTeX
print("## The triangle as Forte labels\n")
print("$$\\begin{array}{c}")
for one_row in chord_stream:
    forte_list = []
    for one_label in one_row:
        new_label = str('\\text{' + str(Pseg(one_label).forte) + '}')
        forte_list.append(new_label)
    print(f"{',\\,\\,\\,'.join(one_label for one_label in forte_list)}\\\\[10pt]")
print("\\end{array}$$\n")

# put the triangle into a Dorico score, one bar per row
my_score = setup_score('Symmetrical triangle of tetrachords', 'piano')
piano = my_score.parts[0]
for measure, one_row in enumerate(chord_stream, 1):
    piano.append(meter.TimeSignature(f'{measure}/4'))
    for one_chord in one_row:
        score_chord = chord.Chord(one_chord)
        score_chord.addLyric(score_chord.forteClassTn)
        piano.append(score_chord)
my_score.show()
