#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zmq
import time
import sys

zmq_ctx = zmq.Context()

publish_zmq_socket = zmq_ctx.socket(zmq.PUB)
publish_zmq_socket.bind(sys.argv[1])

while True:
    time.sleep(1)
    publish_zmq_socket.send(">alfred>hears>"+sys.argv[2])