#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2019/5/9 17:54 
# @Author : wanxin
# @File : PlaybackBycallback.py 
# @Software: PyCharm

import pyaudio
import wave
import time
import sys
import config.RecordConfig as config


wf = wave.open(config.WAVE_OUTPUT_FILENAME, 'rb')

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()
wf.close()

p.terminate()
