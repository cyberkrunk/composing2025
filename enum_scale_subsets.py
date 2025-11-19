# Enumerate all subsets from the 'big four' scales

from music21 import *
from itertools import combinations, permutations
from collections import Counter
import sys

stdout_fileno = sys.stdout
sys.stdout = open("output.txt", "w")

wholetone = (0, 2, 4, 6, 8, 10)
acoustic = (0, 1, 3, 4, 6, 8, 10)
diatonic = (0, 1, 3, 5, 6, 8, 10)
octatonic = (0, 1, 3, 4, 6, 7, 9, 10)

for k in range(1, 9):
    cnt = Counter()
    print("## Subsets of cardinality", k)
    print()
    print("| pcs | Forte name | prime | ic Vector | Common |")
    print("| --- | --- | --- | --- | --- |")
    for i in combinations(octatonic, k):
        print(
            "| ",
            chord.Chord(i).orderedPitchClassesString,
            " | ",
            chord.Chord(i).forteClass,
            " | ",
            chord.Chord(i).primeFormString,
            " | ",
            chord.Chord(i).intervalVectorString,
            " | ",
            chord.Chord(i).commonName,
            " | ",
        )
        cnt[str(chord.Chord(i).forteClass)] += 1
    print("Forte summary:", dict(cnt))
    print()

# Close the file
sys.stdout.close()
# Restore sys.stdout to our old saved file handler
sys.stdout = stdout_fileno
