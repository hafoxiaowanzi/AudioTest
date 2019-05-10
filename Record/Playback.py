#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2019/5/9 17:50 
# @Author : wanxin
# @File : Playback.py 
# @Software: PyCharm


import pyaudio
import config.RecordConfig as config

# CHUNK = 1024

# CHANNELS = 2
# RATE = 44100
# RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(config.WIDTH),
                channels=config.CHANNELS,
                rate=config.RATE,
                input=True,
                output=True,
                frames_per_buffer=config.CHUNK)

print("* recording")

for i in range(0, int(config.RATE / config.CHUNK * config.RECORD_SECONDS)):
    data = stream.read(config.CHUNK)
    stream.write(data, config.CHUNK)

print("* done")

stream.stop_stream()
stream.close()

p.terminate()
