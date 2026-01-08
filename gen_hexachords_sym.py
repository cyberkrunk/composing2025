# ---------------------------------------------------------------------
# This code generates hexachords by taking a trichord from
# gen_trichords_sym and then combining it with 12 transpositions of its
# inversion.
#
# 2026-01-07
# ---------------------------------------------------------------------

import copy
from music21 import *
from classico import Pseg
# from collections import Counter
from cjcomp import pchord_int_label_latex, pchord_int_label, setup_score

# set up the trichord stream
my_chord = Pseg([60, 61, 62])
start_chord = my_chord.pitches
current_chord = []
chord_row = []
trichord_stream = []
hexachord_stream = []
forte_list = []

# create the trichord stream - 55 chords
for outer_voice in range(start_chord[2], start_chord[0] + 12):
    current_chord = copy.deepcopy(start_chord)
    for inner_voice in range(start_chord[1], outer_voice):
        current_chord[1] = inner_voice
        current_chord[2] = outer_voice
        trichord_stream.append(copy.deepcopy(current_chord))

# for each trichord, 1) invert, 2) list all transpositions
# this will total 660 chords
for trichord in trichord_stream:
    rh = Pseg(trichord)
    lh = rh.invert()
    for t in range(12):
        hexachord_stream.append([rh, lh.transpose(t * -1)])

# set up the score
my_score = stream.Score()
my_score.metadata = metadata.Metadata()
my_score.metadata.composer = "Chester Jankowski"
my_score.metadata.title = "Symmetrical hexachords"
piano_rh = stream.PartStaff()
piano_rh.partName = "Piano RH"
piano_lh = stream.PartStaff()
piano_lh.partName = "Piano LH"
piano_lh.insert(0, meter.TimeSignature('12/4'))
piano_rh.insert(0, meter.TimeSignature('12/4'))
my_score.insert(0, piano_rh)
my_score.insert(0, piano_lh)


for index, hexachord in enumerate(hexachord_stream):
    upper = chord.Chord(hexachord[0].pitches)
    if index % 12 == 0:
        upper.addLyric(upper.forteClassTn)
    lower = chord.Chord(hexachord[1].pitches)
    combined =chord.Chord(hexachord[0].pitches + hexachord[1].pitches)
    lower.addLyric(combined.forteClassTn)
    piano_rh.append(upper)
    piano_lh.append(lower)

my_score.show()
