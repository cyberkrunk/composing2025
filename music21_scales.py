from music21 import *

my_major = scale.MajorScale('C')
my_minor = scale.MinorScale('A')
my_harm = scale.HarmonicMinorScale('A')
my_melodic = scale.MelodicMinorScale('A')
my_dorian = scale.DorianScale('D')
my_phrygian = scale.PhrygianScale('E')
my_lydian = scale.LydianScale('F')
my_mixolydian = scale.MixolydianScale('G')
my_locrian = scale.LocrianScale('B')
my_octatonic = scale.OctatonicScale('C')
my_wholetone = scale.WholeToneScale('C')

explore = my_minor
print(f"Pitches: {[p.name for p in explore.getPitches()]}")
print(f"Tonic: {explore.getTonic()}")
print(f"Dominant: {explore.getDominant()}")
print(f"Leading tone: {explore.getLeadingTone()}")


