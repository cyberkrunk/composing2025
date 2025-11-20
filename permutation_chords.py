# Enumerate the permutations with repetition of a given set of
# intervals, then create chords for each perm, while labeling each
# chord with its set name in the lyrics line.
# 2025-11-20

from music21 import stream, expressions, metadata, pitch
from music21 import interval, chord, meter
import itertools

# Define the intervals to be used
interval_pool = [3, 4, 5, 6, 7]
set_size = 4

# Enumerate all permutations with repetition and store them in a list
perms = list(itertools.product(interval_pool, repeat=set_size))
num_chords = str(len(perms))

# Set up score and parts
piano = stream.PartStaff()
piano.partName = "Piano"
te = expressions.TextExpression(num_chords + " chords")
piano.insert(0, te)
score = stream.Score()
score.metadata = metadata.Metadata()
score.metadata.composer = "Chester Jankowski"
score.metadata.title = (
    "Permutation Chords of intervals "
    + str(interval_pool)
    + " and size "
    + str(set_size)
)

# Iterate through the perms and create chords
start_pitch = pitch.Pitch("C4")
for perm in perms:
    interval_label = "".join(map(str, perm))
    current_pitch = start_pitch
    chord_pitches = [start_pitch]
    for i in perm:
        current_pitch = interval.Interval(i).transposePitch(current_pitch)
        chord_pitches.append(current_pitch)
    my_chord = chord.Chord(chord_pitches)
    my_chord.quarterLength = 2
    my_chord.addLyric(interval_label)
    my_chord.addLyric(str(my_chord.forteClassTn))
    # print(interval_label)
    # my_chord.show('text')
    piano.append(my_chord)

# Create and show the score
score.insert(0, meter.TimeSignature("4/4"))
score.insert(0, piano)
score.show()
