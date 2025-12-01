from music21 import *
from cjcomp import int_label, int_sia, plt_circle, pcs_complement


c = chord.Chord("C E- B")
print(c)

print(int_label(c))
print(int_sia(c))
print(pcs_complement(c))

compl = pcs_complement(c)
print(int_label(chord.Chord(compl)))

# foobar = "boobar"

# plt_circle(c, foobar)
