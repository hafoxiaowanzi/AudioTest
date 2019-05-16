#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2019/5/16 18:51 
# @Author : wanxin
# @File : producer.py 
# @Software: PyCharm

import pika
credentials = pika.PlainCredentials('testmq','testmq')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '10.60.79.185',5672,'/',credentials))
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='balance')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='balance',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()