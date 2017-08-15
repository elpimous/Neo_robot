#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


def process():
    wavs = '/home/nvidia/Documents/wav2/'
    wav2 = '/home/nvidia/Documents/wav/'
    for files in os.listdir(wavs):
        A=(files)
        B=(A.replace("record","record."))
        os.system('cp '+wavs+A+' '+wav2+B)


if __name__ == "__main__":
    process()
