# ---------------------------------------------------------------------
# Enumerate all subsets from the most common scales
# ---------------------------------------------------------------------

from music21 import *
from itertools import combinations, permutations
from collections import Counter
from natsort import natsorted
from cjcomp import int_sia
import sys

pentatonic = ["pentatonic", (0, 3, 5, 7, 10)]
dominant_pentatonic = ["dominant-pentatonic", (0, 3, 5, 7, 9)]
wholetone = ["wholetone", (0, 2, 4, 6, 8, 10)]
hexatonic = ["hexatonic", (0, 3, 4, 7, 8, 11)]
acoustic = ["acoustic", (0, 1, 3, 4, 6, 8, 10)]
diatonic = ["diatonic", (0, 1, 3, 5, 6, 8, 10)]
octatonic = ["octatonic", (0, 1, 3, 4, 6, 7, 9, 10)]

scale = hexatonic
size = len(scale[1])

stdout_fileno = sys.stdout
sys.stdout = open("./output/" + str(scale[0]) + "-pc-subsets.md", "w")

print(f"## Subsets of {scale[0]}, {scale[1]}")
print()
print("| pcs | Forte name | prime | sia | ic Vector | Common |")
print("| --- | --- | --- | --- | --- | --- |")
print(
    "| ",
    chord.Chord(scale[1]).orderedPitchClassesString,
    " | ",
    chord.Chord(scale[1]).forteClass,
    " | ",
    chord.Chord(scale[1]).primeFormString,
    " | ",
    int_sia(chord.Chord(scale[1])),
    " | ",
    chord.Chord(scale[1]).intervalVectorString,
    " | ",
    chord.Chord(scale[1]).commonName,
    " |",
)
print()

for k in range(3, size):
    cnt = Counter()
    print("## Subsets of cardinality", k)
    print()
    print("| pcs | Forte name | prime | sia | ic Vector | Common |")
    print("| --- | --- | --- | --- | --- | --- |")
    for i in combinations(scale[1], k):
        print(
            "| ",
            chord.Chord(i).orderedPitchClassesString,
            " | ",
            chord.Chord(i).forteClass,
            " | ",
            chord.Chord(i).primeFormString,
            " | ",
            int_sia(chord.Chord(i)),
            " | ",
            chord.Chord(i).intervalVectorString,
            " | ",
            chord.Chord(i).commonName,
            " |",
        )
        cnt[str(chord.Chord(i).forteClass)] += 1
    items = cnt.items()
    summary = dict(natsorted(items))
    pretty = ", ".join(f"{k}: {v}" for k, v in summary.items())
    print()
    print(f"Forte summary: {pretty}.")
    print()

# Close the file
sys.stdout.close()
# Restore sys.stdout to our old saved file handler
sys.stdout = stdout_fileno
