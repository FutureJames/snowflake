#!/user/bin/env python3
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from luma.core.render import canvas
from PIL import Image
from PIL import ImageFont
import time
import os
import logging

# import user classes
import config
import setup

# link back to SetupClass for readability
device = setup.SetupClass.device


def draw_speech_text(draw, text):
    y_pos = 0
    x_pos = 35 
    draw.text((x_pos, y_pos),
              text=text,
              font=config.JAPAN_FONT,
              fill=config.FG)


def display(string, image_name="snowflake.png"):
    if (len(string) > 14):
        logging.warning("Requested string is too long for spash screen")
    img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            'images',
                                            image_name))
    img = Image.open(img_path).convert(device.mode)
    with canvas(device, background=img, dither=False) as draw:
        draw_speech_text(draw, string)
        
    time.sleep(5)
