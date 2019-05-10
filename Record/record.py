#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2019/5/9 17:20 
# @Author : wanxin
# @File : record.py 
# @Software: PyCharm

import wave
import pyaudio
import config.RecordConfig as config

# import speech_recognition as sr
#
# r = sr.Recognizer()
# mic = sr.Microphone(device_index=1)
#
# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
#     r.recognize_google(audio)



p = pyaudio.PyAudio()

stream = p.open(format=config.FORMAT,
                channels=config.CHANNELS,
                rate=config.RATE,
                input=True,
                frames_per_buffer=config.CHUNK)

print("* recording")

frames = []

for i in range(0, int(config.RATE / config.CHUNK * config.RECORD_SECONDS)):
    data = stream.read(config.CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(config.WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(config.CHANNELS)
wf.setsampwidth(p.get_sample_size(config.FORMAT))
wf.setframerate(config.RATE)
wf.writeframes(b''.join(frames))
wf.close()
