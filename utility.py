#!/user/bin/env python3
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from PIL import ImageFont
import time
import os
import logging
import thread
import subprocess
import sys
import errno

from signal import signal, SIGPIPE, SIG_DFL 
#Ignore SIG_PIPE and don't throw exceptions on it... (http://docs.python.org/library/signal.html)
signal(SIGPIPE,SIG_DFL)



def make_font(name, size):
    font_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             'fonts',
                                             name))
    return ImageFont.truetype(font_path, size)


# helper function for logging and executing simple shell commands
def bash(command):
    try:
        result = subprocess.check_output(command, shell=True)
        return result
    except Exception:
        pass
        #logging.error("Pipe error")


# async alarm for non block status bar updates
def set_alarm(delay, status_timer, name):
    while 1:
        logging.debug("------------------------------Timer- " + name)
        status_timer.set()
        time.sleep(delay)
        thread.exit()

