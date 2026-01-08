# ---------------------------------------------------------------------
# Code to generate a quasi-octatonic scale run that ascends in 8th
# notes until it reaches a target pitch, which sustains for a longer
# note value. Then the process starts again with a higher starting
# pitch.
# ---------------------------------------------------------------------

from music21 import note, articulations
from random import randint
from cjcomp import setup_score

my_score = setup_score("Quasi oct", "Piano")
violin = my_score.parts[0]
stac = articulations.Staccato()

start = 64
target = 88
phrase = 1
shorts = 1
while start < target:
    print(f"{phrase}----------")
    p = start
    shorts = 1
    n = note.Note(p)
    n.quarterLength = 0.25
    n.articulations.append(stac)
    violin.append(n)
    while p < target:
        if p == (target - 1):
            p += 1
            n = note.Note(p)
            if p == target:
                n.quarterLength = (shorts * 0.25)
            else:
                n.quarterLength = 0.25
                n.articulations.append(stac)
            violin.append(n)
            shorts += 1
            print(shorts)
        else:
            step = randint(1, 2)
            p += step
            n = note.Note(p)
            if p == target:
                n.quarterLength = (shorts * 0.25)
            else:
                n.quarterLength = 0.25
                n.articulations.append(stac)
            violin.append(n)
            shorts += 1
            print(shorts)
    start += randint(1, 2)
    phrase += 1

my_score.show()
