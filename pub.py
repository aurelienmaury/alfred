#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zmq
import time
import sys

zmq_ctx = zmq.Context()

publish_zmq_socket = zmq_ctx.socket(zmq.PUSH)
publish_zmq_socket.connect(sys.argv[1])

while True:
    time.sleep(0.5)
    print "sending"
    publish_zmq_socket.send("/alfred/hears/"+sys.argv[2])
