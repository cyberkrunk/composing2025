# ---------------------------------------------------------------------
# Enumerate pc set subsets and supersets
# ---------------------------------------------------------------------

from music21 import *
from itertools import combinations, permutations
from collections import Counter
from natsort import natsorted
from bisect import insort
from cjcomp import int_sia, plt_circle, pcs_complement
import sys

pentatonic = ["pentatonic", [0, 3, 5, 7, 10]]
dominant_pentatonic = ["dominant-pentatonic", [0, 3, 5, 7, 9]]
wholetone = ["wholetone", [0, 2, 4, 6, 8, 10]]
hexatonic = ["hexatonic", [0, 3, 4, 7, 8, 11]]
acoustic = ["acoustic", [0, 1, 3, 4, 6, 8, 10]]
diatonic = ["diatonic", [0, 1, 3, 5, 6, 8, 10]]
octatonic = ["octatonic", [0, 1, 3, 4, 6, 7, 9, 10]]

scale_def = acoustic
scale_name = scale_def[0]
scale_pcs = scale_def[1]
size = len(scale_pcs)

stdout_fileno = sys.stdout
sys.stdout = open("./output/" + str(scale_name) + "-pc-subsets.md", "w")

print(f"## Subsets of {scale_name}, {scale_pcs}")
print()
print("| pcs | Forte name | prime | sia | ic Vector | Common |")
print("| --- | --- | --- | --- | --- | --- |")
print(
    "| ",
    chord.Chord(scale_pcs).orderedPitchClassesString,
    " | ",
    chord.Chord(scale_pcs).forteClass,
    " | ",
    chord.Chord(scale_pcs).primeFormString,
    " | ",
    int_sia(chord.Chord(scale_pcs)),
    " | ",
    chord.Chord(scale_pcs).intervalVectorString,
    " | ",
    chord.Chord(scale_pcs).commonName,
    " |",
)
print()

plt_circle(chord.Chord(scale_pcs), scale_name)

print(f"![](./{scale_name}.png)")
print()

# Enumerate all subsets.
for k in range(3, size):
    cnt = Counter()
    print(f"## Subsets of cardinality: {k}")
    print()
    print("| pcs | Forte name | prime | sia | ic Vector | Common |")
    print("| --- | --- | --- | --- | --- | --- |")
    for i in combinations(scale_pcs, k):
        subset = chord.Chord(i)
        print(
            "| ",
            subset.orderedPitchClassesString,
            " | ",
            subset.forteClass,
            " | ",
            subset.primeFormString,
            " | ",
            int_sia(subset),
            " | ",
            subset.intervalVectorString,
            " | ",
            subset.commonName,
            " |",
        )
        cnt[str(subset.forteClass)] += 1
    items = cnt.items()
    summary = dict(natsorted(items))
    pretty = ", ".join(f"{k}: {v}" for k, v in summary.items())
    print()
    print(f"Summary: {pretty}.")
    print()

# Enumerate all supersets
for k in range(size + 1, 10):
    cnt = Counter()
    print(f"## Supersets of cardinality: {k}")
    print()
    print("| pcs | Forte name | prime | sia | ic Vector | Common |")
    print("| --- | --- | --- | --- | --- | --- |")
    compl = pcs_complement(chord.Chord(scale_pcs))
    pcs_add = k - size
    for i in combinations(compl, pcs_add):
        pcs_new = scale_pcs.copy()
        [insort(pcs_new, add) for add in i]  # Adds new pitches sorted in place
        superset = chord.Chord(pcs_new)
        print(
            "| ",
            superset.orderedPitchClassesString,
            " | ",
            superset.forteClass,
            " | ",
            superset.primeFormString,
            " | ",
            int_sia(superset),
            " | ",
            superset.intervalVectorString,
            " | ",
            superset.commonName,
            " |",
        )
        cnt[str(superset.forteClass)] += 1
        # pcs_new = []
    items = cnt.items()
    summary = dict(natsorted(items))
    pretty = ", ".join(f"{k}: {v}" for k, v in summary.items())
    print()
    print(f"Summary: {pretty}.")
    print()

# Close the file
sys.stdout.close()
# Restore sys.stdout to our old saved file handler
sys.stdout = stdout_fileno
