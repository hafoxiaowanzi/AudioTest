#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2019/5/9 17:40 
# @Author : wanxin
# @File : PlayWav.py 
# @Software: PyCharm

import pyaudio
import wave
import config.RecordConfig as config

# 定义数据流块
CHUNK = 1024

# 只读方式打开wav文件
wf = wave.open(config.WAVE_OUTPUT_FILENAME, 'rb')#(sys.argv[1], 'rb')

p = pyaudio.PyAudio()

# 打开数据流
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# 读取数据
data = wf.readframes(CHUNK)

# 播放
while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

# 停止数据流
stream.stop_stream()
stream.close()

# 关闭 PyAudio
p.terminate()
