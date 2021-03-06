#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2019/5/9 18:08 
# @Author : wanxin
# @File : PlaybackCallbackNoblock.py 
# @Software: PyCharm


"""
PyAudio Example: Make a wire between input and output (i.e., record a
few samples and play them back immediately).

This is the callback (non-blocking) version.
"""

import pyaudio
import time
import config.RecordConfig as config

# WIDTH = 2
# CHANNELS = 2
# RATE = 44100

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    return (in_data, pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(config.WIDTH),
                channels=config.CHANNELS,
                rate=config.RATE,
                input=True,
                output=True,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()

p.terminate()


