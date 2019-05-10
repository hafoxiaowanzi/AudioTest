#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2019/5/9 17:26 
# @Author : wanxin
# @File : Record.config.py 
# @Software: PyCharm

import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

WIDTH = 2