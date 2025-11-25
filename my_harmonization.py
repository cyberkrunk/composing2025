# ---------------------------------------------------------------------
# Python code to automate generation of scale harmonizations.
# 2025-11-25
# ---------------------------------------------------------------------
from music21 import scale, chord, meter, key
from cjcomp import int_label, setup_score

# Define the scale
s = scale.MajorScale("G3")
# s = scale.MelodicMinorScale("C4")
# s = scale.OctatonicScale("F4", 1)  # 1st mode
# s = scale.WholeToneScale("C4")

# Size of the scale is the num pitches in 1 octave
scale_size = len(s.getPitches("C4", "B4"))

# Get the pitches of the scale
scale_pitches = s.getPitches("G3", "C7")

# The chord pattern
generic_chord = [0, 3, 6, 9, 12, 15]

# Size of chord
chord_size = len(generic_chord)

# Create a list to store the harmonized chords
harmonized_chords = []

# Loop through each note of the scale to build a chord
for i in range(scale_size):
    chord_notes = []
    # Create a chord by stacking generic_chord
    for cn in range(chord_size):
        p = scale_pitches[i + generic_chord[cn]]
        p.simplifyEnharmonic(inPlace=True, mostCommon=True)
        chord_notes.append(p)
    c = chord.Chord(chord_notes)
    harmonized_chords.append(c)

# Set up a score, iterate through and label the chords
my_score = setup_score("Quartal hexachords", "Guitar")
part = my_score.parts[0]
part.insert(key.Key("G", "major"))
for c in harmonized_chords:
    c.quarterLength = 4
    part.append(c)
    c.addLyric(int_label(c))
    c.addLyric(str(c.forteClassTn))
ts = meter.TimeSignature(str(scale_size) + "/1")
ts.style.hideObjectOnPrint = True
part.insert(0, ts)
my_score.show()
