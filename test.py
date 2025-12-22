from music21 import *
from cjcomp import int_label, int_sia, plt_circle, pcs_complement
from bisect import *
from pctheory import pitch, pcseg, pcset, transformations

# find the TnI relation of two sets

A = pcset.make_pcset12(0, 3, 7, 9)
B = pcset.make_pcset12(2, 5, 9, 11)

C = transformations.find_utos(A, B)

print(C)
