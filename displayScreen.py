#!/user/bin/env python3
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from luma.core.render import canvas
import time
import RPi.GPIO as GPIO  # noqa: N814

import logging
import config
import setup
import statusbar

# link back to SetupClass for readability
device = setup.SetupClass.device


def draw_list(draw, text):
    edge_left = 0
    y_pos = 10
    spacing = 10
    for line in text:
        draw.text((edge_left, y_pos),
                  text=line,
                  font=config.TEXT_FONT,
                  fill=config.FG)
        y_pos += spacing


# main entry point for this class, generally from menuClass.startMenu()
def display(text, wait=True):
    logging.debug("ENTERING DISPLAY SCREEN")
    time.sleep(0.2)  # prevent instant selection from new menu

    status = statusbar.init()
    alarm_clock = 0
    while 1:
        if (time.time() > alarm_clock):
            alarm_clock = time.time() + config.STATUS_FREQUENCY
            status = statusbar.get_status(status)

        # handle keypresses
        # user hits cancel
        if (GPIO.input(config.KEY_CANCEL_PIN) == False):  # noqa: E712
            return None
        if (GPIO.input(config.KEY_UP_PIN) == False):  # noqa: E712
            return None
        if (GPIO.input(config.KEY_SELECT_PIN) == False):  # noqa: E712
            return None
        if (GPIO.input(config.KEY_DOWN_PIN) == False):  # noqa: E712
            return None

        # paint the screen
        with canvas(device, dither=False) as draw:
            statusbar.draw(draw, status)
            draw_list(draw, text)


        # wait is False if this is a loading screen
        if (wait == False):
            return None

        # debounce keys
        time.sleep(0.1)
