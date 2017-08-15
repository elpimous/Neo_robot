#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import sys
import scipy.io.wavfile as wav
from deepspeech.model import Model
import time
print('imports ok')

model2 = '/home/nvidia/DeepSpeech/data/ldc93s1/model/output_graph.pb'
micro2 = '/home/nvidia/DeepSpeech/data/ldc93s1/LDC93S1.wav'

ds = Model(model2, 26, 9) #model link, cepstrum, context
print('Model ok')


while 1:
    print('lecture wav')
    fs, audio = wav.read(micro2)
    print(ds.stt(audio, fs))


