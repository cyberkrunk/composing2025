# ----------------------------------------------------------------------------
# This code models the pitch sequence in Arvo Part's Cantus in Memory of
# Benjamin Britten, the first violin part
# ----------------------------------------------------------------------------

# This defines a descending natural minor scale in 6 octaves
scale_base = [0, -2, -4, -5, -7, -9, -10]
scale_full = scale_base.copy()
for octave in [-12, -24, -36, -48, -60]:
    for note in range(len(scale_base)):
        scale_full.append(octave + scale_base[note])

# Construct the pitch stream in MIDI note numbers
stream = []
sequence = [94]
stream.append(sequence)
for i in range(1, 21):
    sequence = []
    for j in range(0, i + 1):
        sequence.append(94 + scale_full[j])
    stream.append(sequence)
print(stream)
print(f"The full scale range: {scale_full}")
