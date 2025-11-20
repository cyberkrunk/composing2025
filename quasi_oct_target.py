# Code to generate a quasi-octatonic scale run that ascends in 8th notes
# until it reaches a target pitch, which sustains for a longer note value.
# Then the process starts again with a higher starting pitch.

import music21 *

start = 60
target =  