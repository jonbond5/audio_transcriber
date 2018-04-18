import pyaudio, wave, sys
import numpy as np
import matplotlib.pyplot as plt
import threading

songname = "songs\\sample.wav"
song = wave.open(songname, 'rb')
p = pyaudio.PyAudio()

if len(sys.argv) < 2:
    chunk = song.getnframes()
else:
    chunk = sys.argv[1]

stream = p.open(format=p.get_format_from_width(song.getsampwidth()),
                channels=song.getnchannels(),
                rate=song.getframerate(),
                output=True)

def play(data, chunk=1024):
    song.rewind()
    while len(data) > 0:
        stream.write(data)
        data = song.readframes(chunk)

data = song.readframes(chunk)
print "Converting bytes to ints..."
data_numerically = [ord(x) for x in data]
channel_1 = data_numerically[::2]
channel_2 = data_numerically[1::2]
print "FFT..."
fftdata = abs(np.fft.fft(data_numerically))
print "FFT Frequencies..."
freq = np.fft.fftfreq(len(data_numerically))
# https://stackoverflow.com/questions/604453/analyze-audio-using-fast-fourier-transform