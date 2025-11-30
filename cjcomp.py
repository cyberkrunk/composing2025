# ---------------------------------------------------------------------
# My composition module, a collection of functions.
# 2025-11-25
# ---------------------------------------------------------------------
from music21 import note, interval, stream, metadata
import matplotlib.pyplot as plt
import math
import numpy as np


def int_label(my_chord):
    """
    Takes a music21 chord and returns an interval label like <3-4>

    :param my_chord: chord
    """
    chord_size = len(my_chord.pitches)
    for p in my_chord.pitches:
        p.simplifyEnharmonic(inPlace=True, mostCommon=True)
        p.octave = 4
    interval_list = []
    for i in range(chord_size - 1):
        chord_interval = interval.Interval(my_chord[i], my_chord[i + 1]).semitones
        interval_list.append(chord_interval)
    interval_label = "<" + "-".join(map(str, interval_list)) + ">"
    return interval_label


def int_sia(my_chord):
    """
    Takes a music21 chord and returns an interval sia like <3-4-5>

    :param my_chord: chord
    """
    chord_size = len(my_chord.pitches)
    for p in my_chord.pitches:
        p.simplifyEnharmonic(inPlace=True, mostCommon=True)
        p.octave = 4
    interval_list = []
    for i in range(chord_size - 1):
        chord_interval = interval.Interval(my_chord[i], my_chord[i + 1]).semitones
        interval_list.append(chord_interval)
    last_interval = interval.Interval(
        my_chord[-1], my_chord[0].transpose(interval.Interval("P8"))
    ).semitones
    interval_list.append(last_interval)
    interval_sia = "<" + "-".join(map(str, interval_list)) + ">"
    return interval_sia


def plt_circle(my_chord, scale_name):
    """
    Takes a music21.chord.Chord and plots it on a circle diagram

    :param my_chord: chord
    """
    # Get the chord ready.
    for p in my_chord.pitches:
        p.simplifyEnharmonic(inPlace=True, mostCommon=True)
        p.octave = 0
    pcs = [p.pitchClass for p in my_chord.pitches]

    # Draw a unit circle using the parametric equation;
    # use numpy to generate 100 numbers between 0 and 2*pi.
    theta = np.linspace(0, 2 * np.pi, 100)
    r = 1  # set the radius to one

    # The x and y coordinates are the cos and sin of theta.
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Plot the circle.
    figure, axes = plt.subplots(1)
    axes.plot(x, y, "black")
    axes.set_aspect(1)
    plt.axis("off")
    axes.grid(False)
    axes.set_xticks([])
    axes.set_yticks([])

    # Dictionary for the clock positions.
    dict = {
        "0": [0, 1],
        "1": [1 / 2, math.sqrt(3) / 2],
        "2": [math.sqrt(3) / 2, 1 / 2],
        "3": [1, 0],
        "4": [math.sqrt(3) / 2, -1 / 2],
        "5": [1 / 2, -math.sqrt(3) / 2],
        "6": [0, -1],
        "7": [-1 / 2, -math.sqrt(3) / 2],
        "8": [-math.sqrt(3) / 2, -1 / 2],
        "9": [-1, 0],
        "10": [-math.sqrt(3) / 2, 1 / 2],
        "11": [-1 / 2, math.sqrt(3) / 2],
    }

    # Plot the position markers.
    for i in range(12):
        axes.plot(
            dict[str(i)][0],
            dict[str(i)][1],
            marker="o",
            markerfacecolor="white",
            color="black",
            markersize="8",
        )

    # Plot the position labels.
    for i in range(12):
        axes.text(
            dict[str(i)][0] * 1.1,
            dict[str(i)][1] * 1.1,
            str(i),
            ha="center",
            va="center",
        )

    # # Define a pc set and plot some points
    # pcs = [0, 1, 2, 4, 6, 7, 8, 10]

    # iterate through pairs
    for a in range(len(pcs) - 1):
        axes.plot(
            [dict[str(pcs[a])][0], dict[str(pcs[a + 1])][0]],
            [dict[str(pcs[a])][1], dict[str(pcs[a + 1])][1]],
            "ko-",
        )

    # now plot the last pair back to 0
    axes.plot(
        [dict[str(pcs[len(pcs) - 1])][0], dict[str(pcs[0])][0]],
        [dict[str(pcs[len(pcs) - 1])][1], dict[str(pcs[0])][1]],
        "ko-",
    )
    plt.savefig(f"./output/{scale_name}.png")


def setup_score(title, instrument):
    """
    Returns a basic music21 score object

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
