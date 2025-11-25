from music21 import note, chord, interval, stream
from cjcomp import setup_score

my_score = setup_score("Holy fucking shitballs", "Guitar")
part = my_score.parts[0]
part.append(note.Note("C5"))
my_score.show()
