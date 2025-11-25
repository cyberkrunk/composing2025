# ---------------------------------------------------------------------
# My composition module, a collection of functions.
# 2025-11-25
# ---------------------------------------------------------------------
from music21 import note, interval, stream, metadata


def int_label(my_chord):
    """
    Takes a music21 chord and returns an interval label like <3-4>

    :param my_chord: chord
    """
    chord_size = len(my_chord.pitches)
    interval_list = []
    for i in range(chord_size - 1):
        chord_interval = interval.Interval(my_chord[i], my_chord[i + 1]).semitones
        interval_list.append(chord_interval)
        interval_label = "<" + "-".join(map(str, interval_list)) + ">"
    return interval_label


def setup_score(title, instrument):
    """
    Returns a basic score object

    :param title: Title
    :param instrument: Instrument name
    """
    my_score = stream.Score()
    my_score.metadata = metadata.Metadata()
    my_score.metadata.composer = "Chester Jankowski"
    my_score.metadata.title = title
    part = stream.PartStaff()
    part.partName = instrument
    my_score.insert(0, part)
    return my_score
