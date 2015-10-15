#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'amaury'

import os
import zmq
import argparse

from brain import Brain

EAR_CHANNEL = ">ears>perceive>"
SPEECH_RECOG_CHANNEL = ">speech-recog>"

def parse_cli():
    parser = argparse.ArgumentParser(description='alfred-speech-recog')

    parser.add_argument('-b',
                        dest="brain_path", metavar='BRAIN_PATH', type=str,
                        help='ALICE brain file path', required=True)

    parser.add_argument('-m',
                        dest="modules_path", metavar="MODULES_PATH", type=str,
                        help='ALICE modules directory path', required=True)

    parser.add_argument('-i',
                        dest="zmq_in_addr", metavar="0MQ_INPUT_ADDR", type=str,
                        help='zero MQ ears output address', required=True)

    parser.add_argument('-o',
                        dest="zmq_out_addr", metavar="0MQ_OUTPUT_ADDR", type=str,
                        help='zero MQ publish address', required=True)

    return parser.parse_args()


def main():

    args = parse_cli()
    zmq_ctx = zmq.Context()

    from_ears = init_input_from_ears(args.zmq_in_addr, zmq_ctx)

    publish_sock = zmq_ctx.socket(zmq.PUB)
    publish_sock.bind(args.zmq_out_addr)

    brain = Brain(args.modules_path, args.brain_path)

    brain.load_brain()
    brain.load_session()

    try:
        while True:
            print "zero-brain loop"

            message = receive(from_ears)

            brain_response = brain.kernel.respond(message, brain.session_name)

            if brain_response:
                print "zero-brain:say:"+SPEECH_RECOG_CHANNEL+brain_response
                publish_sock.send(SPEECH_RECOG_CHANNEL+brain_response)

    except KeyboardInterrupt:
        pass
    finally:
        brain.save_session()


def init_input_from_ears(zmq_in_addr, zmq_ctx):
    from_ears = zmq_ctx.socket(zmq.SUB)
    from_ears.setsockopt(zmq.SUBSCRIBE, EAR_CHANNEL)
    from_ears.connect(zmq_in_addr)
    return from_ears


def receive(bus):
    raw_message = bus.recv()

    print "zero-brain:heard:"+raw_message

    return raw_message.replace(EAR_CHANNEL, "", 1)

if __name__ == "__main__":
    main()
