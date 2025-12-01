from music21 import *
from itertools import combinations, permutations
from collections import Counter
from natsort import natsorted
from cjcomp import int_sia, plt_circle, pcs_complement

scale_def = ["Major 7th chord", [0, 4, 7, 11]]
size = len(scale_def[1])

for k in range(size + 1, 10):
    cnt = Counter()
    print(f"## Supersets of cardinality: {k}")
    print()
    print("| pcs | Forte name | prime | sia | ic Vector | Common |")
    print("| --- | --- | --- | --- | --- | --- |")
    compl = pcs_complement(chord.Chord(scale_def[1]))
    pcs_add = k - size
    for i in combinations(compl, pcs_add):
        pcs_new = scale_def[1] + list(i)
        pcs_new.sort()
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
    items = cnt.items()
    summary = dict(natsorted(items))
    pretty = ", ".join(f"{k}: {v}" for k, v in summary.items())
    print()
    print(f"Summary: {pretty}.")
    print()
