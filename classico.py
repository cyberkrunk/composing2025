from collections import deque
from random import sample
from music21 import chord


class Pseg:

    def __init__(self, pitches: list[int]):
        self.pitches = pitches
        self.intervals = [pitch - self.pitches[0] for pitch in self.pitches]
        self.size = len(self.pitches)
        self.range = [min(self.pitches), max(self.pitches)]
        self.ambitus = self.range[1] - self.range[0]
        self.pcseg = [pitch % 12 for pitch in self.pitches]
        self.pcset = {pitch % 12 for pitch in self.pitches}
        self.cardinality = len(self.pcset)
        self.forte = chord.Chord(self.pcset).forteClassTn

    def __str__(self):
        return str(self.pitches)

    def __repr__(self):
        return str(self.pitches)

    def __call__(self):
        return type(self)(self.pitches)

    def transpose(self, transposition: int):
        return type(self)([pitch + transposition for pitch in self.pitches])

    def invert(self):
        return type(self)([self.pitches[0] * 2 - pitch for pitch in self.pitches])

    def tni(self, transposition: int):
        return type(self)(
            [self.pitches[0] * 2 - pitch + transposition for pitch in self.pitches]
        )

    def retrograde(self):
        return type(self)(self.pitches[::-1])

    def rot(self, rotation: int):
        dek = deque(self.pitches)
        dek.rotate(rotation)
        return type(self)(list(dek))

    def scramble(self):
        return type(self)(sample(self.pitches, k=self.size))
