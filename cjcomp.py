# ---------------------------------------------------------------------
# My composition module, a collection of functions.
# 2025-11-25
# ---------------------------------------------------------------------
from music21 import note, interval, chord, stream, metadata
import matplotlib.pyplot as plt
import math
import numpy as np

# ---------------------------------------------------------------------
# Utils
# ---------------------------------------------------------------------


def chord_2_pchord(my_chord):
    """
    Converts a music21.chord.Chord to a pchord

    :param my_chord: chord.Chord
    """
    pchord = [p.midi for p in my_chord.pitches]
    return pchord


def pchord_2_chord(my_pchord):
    """
    Converts a pchord to a music21.chord.Chord

    :param my_pchord: pchord
    """
    my_chord = chord.Chord(my_pchord)
    return my_chord


# ---------------------------------------------------------------------
# Labels
# ---------------------------------------------------------------------


def int_label(my_chord):
    """
    Takes a music21.chord.Chord and returns an interval label like <3-4>

    :param my_chord: chord
    """
    chord_size = len(my_chord.pitches)
    pcs = [p.pitchClass for p in my_chord.pitches]
    interval_list = []
    for i in range(chord_size - 1):
        chord_interval = pcs[i + 1] - pcs[i]
        interval_list.append(chord_interval)
    interval_label = "<" + "-".join(map(str, interval_list)) + ">"
    return interval_label


def int_sia(my_chord):
    """
    Takes a music21.chord.Chord and returns an interval sia like <3-4-5>

    :param my_chord: chord
    """
    chord_size = len(my_chord.pitches)
    pcs = [p.pitchClass for p in my_chord.pitches]
    interval_list = []
    for i in range(chord_size - 1):
        chord_interval = pcs[i + 1] - pcs[i]
        interval_list.append(chord_interval)
    last_interval = (pcs[0] + 12) - pcs[-1]
    interval_list.append(last_interval)
    interval_sia = "<" + "-".join(map(str, interval_list)) + ">"
    return interval_sia


def pchord_int_label(my_pchord: list[int]) -> str:
    """
    Generates an interval list label for a pchord which is
    a chord in p-space, ordered from low to high

    :param my_pchord: Description
    """
    interval_list = []
    for i in range(len(my_pchord) - 1):
        interval = my_pchord[i + 1] - my_pchord[i]
        interval_list.append(interval)
    label = "<" + "-".join(map(str, interval_list)) + ">"
    return label


# ---------------------------------------------------------------------
# Operators
# ---------------------------------------------------------------------


def pcs_complement(my_chord):
    """
    Takes a music21.chord.Chord and returns its complement
    as a list of pcs

    :param my_chord: chord
    """
    A = [p.pitchClass for p in my_chord.pitches]  # The chord.
    U = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # The aggregate.
    C = [pc for pc in U if pc not in A]  # The complement.
    return C


def pseg_pcset_cardinality(my_pseg: list[int]) -> int:
    """
    Takes a pseg and returns the cardinality of its pitch class set

    :param my_pseg: pseg
    :type my_pseg: list[int]
    :return: cardinality of pitch class set
    :rtype: int
    """
    return len({p % 12 for p in my_pseg})


def pseg_invert(my_pseg: list[int]) -> list[int]:
    """
    Invert a pseg

    :param my_pseg: pseg
    """
    # create an interval list
    pseg_size = len(my_pseg)
    interval_list = [
        0,
    ]
    for i in range(pseg_size - 1):
        pseg_interval = my_pseg[i + 1] - my_pseg[i]
        interval_list.append(pseg_interval)

    # invert the interval list
    interval_list_inverted = [interval * -1 for interval in interval_list]

    # create the inverted pseg
    pseg_inverted = [
        my_pseg[0],
    ]  # the starting pitch
    for i in range(1, pseg_size):
        p = pseg_inverted[i - 1] + interval_list_inverted[i]
        pseg_inverted.append(p)
    return pseg_inverted


def pseg_transpose(my_pseg: list[int], transposition_interval: int) -> list[int]:
    """
    Takes a pseg and returns a transposed pseg

    :param my_pseg: pseg, transposition interval
    """
    pseg_transposed = [pitch + transposition_interval for pitch in my_pseg]
    return pseg_transposed


# ---------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------


def plt_circle(my_chord, scale_name):
    """
    Takes a music21.chord.Chord and plots it on a circle diagram

    :param my_chord: chord
    """
    # Get the chord ready.
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


# ---------------------------------------------------------------------
# Score utils
# ---------------------------------------------------------------------


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
