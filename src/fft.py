# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este archivo temporal se encuentra aquí:
/home/pancho/.spyder2/.temp.py
"""

import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
fs, data = wavfile.read('../audios/SonidoA4Piano.wav') # load the data
a = data.T[0] # this is a two channel soundtrack, I get the first track
#plt.plot(a,'r') 
#plt.show()
c = fft(a) # create a list of complex number
d = len(c)/2  # you only need half of the fft list
plt.plot(abs(c[:6000]),'r') 
plt.show()