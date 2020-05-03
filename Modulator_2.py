import os
import librosa
import numpy as np
from scipy.io.wavfile import write
from thinkdsp import read_wave, CosSignal



wave = read_wave('105977__wcfl10__favorite-station.wav')

carrier_sig = CosSignal(freq=440)
carrier_wave = carrier_sig.make_wave(duration=wave.duration, framerate=wave.framerate)

modulated = wave * carrier_wave 
# amplitude modulation - multiplying the input wave by a carrier wave in the time domain
modulated.make_audio()
modulated.play('out1.wav')




y, sr = librosa.load('105977__wcfl10__favorite-station.wav', sr=44100) # y is a numpy array of the wav file, sr = sample rate
y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=-8) # shifted by n_steps
# pitch shift - a step is equal to a semitone
write('out2.wav', 44100, y_shifted)
print('Writing out2.wav')



#combining amplitude modulation and pitch shift together for greater voice modulation
y, sr = librosa.load('out1.wav', sr=44100)
y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=-8) 

write('out1_2.wav', 44100, y_shifted)
print('Writing out1_2.wav')
