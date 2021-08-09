import numpy as np
from numpy import pi, sin
import sounddevice as sd
from basic_sd.helpers.constants import sample_rate


def sine_wave(frequency: int, duration: int):
    return sin(frequency * np.linspace(0, 2 * pi * duration, int(duration * sample_rate)))


for i in range(400, 10000, 10):
    print(i)
    sd.play(sine_wave(i, 0.2)*0.5, sample_rate)
    sd.wait()
