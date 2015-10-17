#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'amaury'

import zmq
import os
import sys
import argparse

VOICE_CHANNEL = "/alfred/says/"


def parse_cli():
    parser = argparse.ArgumentParser(description='alfred-ears')

    parser.add_argument('-i',
                        dest="zmq_in_addr", metavar='0MQ_INPUT_ADDR', type=str,
                        help='zero MQ address of spinal-cord''s output', required=True)

    parser.add_argument('--espeak-path',
                        dest="espeak_path", metavar="PATH", type=str,
                        help='espeak executable path', required=True)

    parser.add_argument('--sox-path',
                        dest="sox_path", metavar="PATH", type=str,
                        help='sox executable path', required=True)

    parser.add_argument('--mbrola-path',
                        dest="mbrola_path", metavar="PATH", type=str,
                        help='mbrola executable path')

    parser.add_argument('--mbrola-voice',
                        dest="mbrola_voice", metavar="PATH", type=str,
                        help='mbrola voice path')

    return parser.parse_args()


def main():
    args = parse_cli()

    context = zmq.Context()
    sock = context.socket(zmq.SUB)
    sock.setsockopt(zmq.SUBSCRIBE, VOICE_CHANNEL)
    sock.connect(args.zmq_in_addr)

    text_to_speech_command_line = build_text_to_speech_cmdline(args)

    while True:
        print "alfred-voice ready on " + args.zmq_in_addr

        message = sock.recv()

        if message and message.startswith(VOICE_CHANNEL):
            clean_message = message.replace(VOICE_CHANNEL, "", 1)
            if clean_message:
                cmd = text_to_speech_command_line % clean_message
                print cmd
                os.system(cmd)


def build_text_to_speech_cmdline(args):
    sox_filter = 'wav'

    if 'darwin' == sys.platform:
        sox_filter = 'coreaudio'

    text_to_speech_command_line = args.espeak_path + ' -v fr-fr -s 150 --stdout "%s" '
    text_to_speech_command_line += ' | '

    if args.mbrola_path and args.mbrola_voice:
        sox_filter = 'au'
        text_to_speech_command_line += args.mbrola_path + ' -t 1.2 -f 1.4 -e ' + args.mbrola_voice + ' - -.au '
        text_to_speech_command_line += ' | '

    if 'darwin' == sys.platform:
        text_to_speech_command_line += args.sox_path + ' - --no-show-progress -t ' + sox_filter + ' bass +1 pitch -300 echo 0.8 0.4 99 0.3'
    else:
        text_to_speech_command_line += args.sox_path + ' --no-show-progress -t ' + sox_filter + ' - bass +1 pitch -300 echo 0.8 0.4 99 0.3'
        
    return text_to_speech_command_line


if __name__ == "__main__":
    main()
