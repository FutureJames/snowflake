#!/user/bin/env python3

from luma.core.interface.serial import spi, i2c
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


    # configure screen stuff
    GPIO.setmode(GPIO.BCM)
    if (config.SCREEN == 0):
        logging.info("SPI Screen")
        serial = spi(device=0,
                     port=0,
                     bus_speed_hz=8000000,
                     transfer_size=4096,
                     #gpio_CS=config.CS_PIN,
                     gpio_DC=config.DC_PIN,
                     gpio_RST=config.RST_PIN)
    elif (config.SCREEN == 1):
        logging.info("I2C Screen")
        GPIO.setup(config.RST_PIN,GPIO.OUT)
        GPIO.output(config.RST_PIN,GPIO.HIGH)
        serial = i2c(port=1, address=config.I2C_ADDRESS)
    device = sh1106(serial, rotate=config.ROTATION)



    # key pins defined in constant.py
    GPIO.setup(config.KEY_CANCEL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(config.KEY_UP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(config.KEY_SELECT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(config.KEY_DOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    logging.info("SetupClass Initialized")
