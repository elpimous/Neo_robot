#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import fnmatch

directory = '/home/nvidia/deepspeech/DeepSpeech/data/deepspeech_material/dev/'

def process():
    # read existing sentences file
    sentenceTextFile = open('/home/nvidia/deepspeech/DeepSpeech/data/deepspeech_material/dev/valid_corrige.txt', 'rb')
    sentences = sentenceTextFile.readlines()

    transcriptions = open('/home/nvidia/deepspeech/DeepSpeech/data/deepspeech_material/dev/valid.csv', 'wb')

    wavDir = directory

    wavs = directory+'record.'
    
    content = len(fnmatch.filter(os.listdir(wavDir), '*.wav'))
    
    transcriptions.write('wav_filename,wav_filesize,transcript\n')
    for i in range(content):

        wavPath = wavs+str(i+1)+'.wav'
        wavSize=(os.path.getsize(wavPath))
        transcript=sentences[i]
        
        transcriptions.write(wavPath+","+str(wavSize)+','+transcript)
    transcriptions.close()
        
if __name__ == "__main__":
    process()
