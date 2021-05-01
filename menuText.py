#!/user/bin/env python3
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from luma.core.render import canvas
import time
import logging
import RPi.GPIO as GPIO  # noqa: N814

import config
import setup
import statusbar
# import utility

# link back to SetupClass for readability
device = setup.SetupClass.device

# number of rows to display on screen
NUM_ROWS = 3


def draw_list(draw, text, selected, top_position):
    y_pos = 12
    edge_left = 0
    edge_right = 128
    index = 0
    spacing = 16

    # handle short lists
    if top_position+NUM_ROWS < len(text):
        bottom_position = top_position+NUM_ROWS
    else:
        bottom_position = len(text)

    # scroll to correct section
    for line in range(top_position, bottom_position):
        if (index == selected):
            text_color = config.BG
            cursor_color = config.FG
        else:
            text_color = config.FG
            cursor_color = config.BG

        draw.rectangle((edge_left, y_pos, edge_right, y_pos+spacing),
                       outline=cursor_color,
                       fill=cursor_color)
        draw.text((edge_left, y_pos),
                  text=text[line].value,
                  font=config.LIST_FONT,
                  fill=text_color)
        index += 1
        y_pos += spacing


# main entry point for this class, generally from menuClass.startMenu()
def display(text):
    time.sleep(0.2)  # prevent instant selection from new menu
    selected = 0
    top_position = 0

    status = statusbar.init()
    alarm_clock = 0
    while 1:
        if (time.time() > alarm_clock):
            alarm_clock = time.time() + config.STATUS_FREQUENCY
            status = statusbar.get_status(status)

        # handle keypresses
        if (GPIO.input(config.KEY_UP_PIN) == False):  # noqa: 712
            selected -= 1
        if (GPIO.input(config.KEY_DOWN_PIN) == False):  # noqa: 712
            selected += 1
        if (GPIO.input(config.KEY_SELECT_PIN) == False):  # noqa: 712
            return selected + top_position
        if (GPIO.input(config.KEY_CANCEL_PIN) == False):  # noqa: 712
            return None
        # list scroll logic
        if (selected >= len(text)-1):
            selected = len(text)-1
        if (selected > (NUM_ROWS-1)):
            selected = (NUM_ROWS-1)
            if (len(text) > (top_position+NUM_ROWS)):
                top_position += 1
                logging.debug("Top position changed> " + str(top_position))
        if (selected < 0):
            selected = 0
            if (top_position > 0):
                top_position -= 1
                logging.debug("Top position changed< " + str(top_position))

        # paint the screen
        with canvas(device, dither=False) as draw:
            statusbar.draw(draw, status)
            draw_list(draw, text, selected, top_position)

        # debounce keys
        time.sleep(0.1)
