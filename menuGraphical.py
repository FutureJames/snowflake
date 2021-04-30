#!/user/bin/env python3
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from luma.core.render import canvas
from PIL import Image
# from PIL import ImageFont
import time
import os
import RPi.GPIO as GPIO  # noqa: N814
import logging

# user imports
import config
import setup
import statusbar
# import utility

# link back to SetupClass for readability
device = setup.SetupClass.device


def draw_speech_bubble(draw, bubble_height):
    edge_right = 127
    edge_bottom = 12 + (17 * bubble_height)
    bubble_left = 75
    bubble_top = 12
    # bubble
    draw.rectangle((bubble_left, bubble_top, edge_right, edge_bottom),
                   outline=config.FG,
                   fill=config.BG)
    # pointer
    draw.polygon([(bubble_left, bubble_top+8),
                  (bubble_left, bubble_top+18),
                  (bubble_left-5, bubble_top+20)],
                 outline=config.FG,
                 fill=config.BG)
    draw.line((bubble_left, bubble_top+10, bubble_left, bubble_top+17),
              fill=config.BG)


def draw_speech_text(draw, text):
    draw_speech_bubble(draw, len(text))
    y_pos = 0
    spacing = 15
    upper_left = 82
    for line in text:
        y_pos += spacing
        draw.text((upper_left, y_pos),
                  text=line,
                  font=config.TEXT_FONT,
                  fill=config.FG)
    # continue icon
    draw.text((120, 52), text="\uf0da",
              font=config.SYMBOL_FONT,
              fill=config.FG)


def display(text):
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            'images',
                                            'snowflake.png'))
    img = Image.open(img_path).convert(device.mode)

    status = statusbar.init()
    alarm_clock = 0
    while 1:
        if (time.time() > alarm_clock):
            alarm_clock = time.time() + config.STATUS_FREQUENCY
            status = statusbar.get_status(status)

        # user exists screen
        if (GPIO.input(config.KEY_PRESS_PIN) == False):  # noqa: 712
            logging.debug("exiting ")
            return None

        with canvas(device, background=img, dither=False) as draw:
            statusbar.draw(draw, status)
            draw_speech_text(draw, text)
        time.sleep(0.1)
