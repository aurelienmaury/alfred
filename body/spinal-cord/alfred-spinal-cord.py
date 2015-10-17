#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'amaury'

import zmq
import argparse


def parse_cli():
    parser = argparse.ArgumentParser(description='alfred-spinal-cord')

    parser.add_argument('-i',
                        dest="zmq_in_addr", metavar="0MQ_INPUT_ADDR", type=str,
                        help='zero MQ input address (pull)', required=True)

    parser.add_argument('-o',
                        dest="zmq_out_addr", metavar="0MQ_OUTPUT_ADDR", type=str,
                        help='zero MQ output address (pub)', required=True)

    return parser.parse_args()


def main():
    args = parse_cli()
    zmq_ctx = zmq.Context()

    input_sock = zmq_ctx.socket(zmq.PULL)
    input_sock.bind(args.zmq_in_addr)

    output_sock = zmq_ctx.socket(zmq.PUB)
    output_sock.bind(args.zmq_out_addr)

    try:
        while True:
            msg = input_sock.recv()
            print "Relayed to nervous system: " + msg
            output_sock.send(msg)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
