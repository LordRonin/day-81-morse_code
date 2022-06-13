import math
import struct
import wave


class AudioCreator:
    """ A simple class to create wav audio file with equal length sinowave sound and gaps.
    """
    def __init__(self, sample_rate=44100, duration=500, frequency=440):
        self._audio = []
        self._sample_rate = sample_rate
        self._frequency = frequency
        self._samples_per_unit = duration * (sample_rate / 1000)
        self._duration = duration
        self._volume = 1

    def add_unit_gap(self):
        for _ in range(int(self._samples_per_unit)):
            self._audio.append(0.0)

    def add_unit_sound(self):
        for x in range(int(self._samples_per_unit)):
            self._audio.append(
                self._volume * math.sin(4 * math.pi * self._frequency * (x / self._sample_rate))
            )

    def save_file(self, filename: str):
        wav_file = wave.open(filename, 'wb')

        # wav parameters.
        nchannels = 1
        sampwidth = 2
        nframes = len(self._audio)
        comptype = 'NONE'
        compname = 'not compressed'
        wav_file.setparams((nchannels, sampwidth, self._sample_rate, nframes, comptype, compname))

        # WAV files here are using short, 16 bit, signed integers for the
        # sample size.  So we multiply the floating point data we have by 32767
        # the maximum value for a short integer
        for sample in self._audio:
            wav_file.writeframes(struct.pack('h', int(sample * 32767)))

        wav_file.close()
