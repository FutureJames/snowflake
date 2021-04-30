#!/user/bin/env python3

from luma.core.interface.serial import spi
from luma.oled.device import sh1106
import RPi.GPIO as GPIO  # noqa: N814

# python imports
import logging

# user imports
import config


class SetupClass:

    # setup logs to be used in all python files, reset on each run
    logging.basicConfig(filename='logging.log',
                        filemode='w',
                        encoding='utf-8',
                        level=logging.DEBUG)

    GPIO.setwarnings(False)
    serial = spi(device=0,
                 port=0,
                 bus_speed_hz=8000000,
                 transfer_size=4096,
                 gpio_DC=24,
                 gpio_RST=25)
    device = sh1106(serial, rotate=2)  # sh1106

    GPIO.setmode(GPIO.BCM)

    # key pins defined in constant.py
    GPIO.setup(config.KEY_UP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(config.KEY_DOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(config.KEY_LEFT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(config.KEY_RIGHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(config.KEY_PRESS_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(config.KEY1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(config.KEY2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(config.KEY3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    logging.info("SetupClass Initialized")
