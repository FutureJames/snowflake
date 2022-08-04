#!/user/bin/env python3
# -*- coding:utf-8 -*-
""" Docstring """
from __future__ import unicode_literals
import time
import logging

import RPi.GPIO as GPIO  # noqa: N814

import setup
import menuClass
import menuGraphical
import displayScreen
import splashScreen
import config

def main():
    """Docstring"""
    logging.info("entering main()")
    setup.SetupClass.device.contrast(255)
#    splashScreen.display("スノーフレーク", "snowflake.png")
#    splashScreen.display("12345678901234", "Snowflake_A.png")
#
    text = ["Tap BACK to begin"]
    text2 = ["Hey m8", "Let's", "Play"]
#    menuGraphical.display(text2)
#    displayScreen.display(text)

#    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    menu_a = [menuClass.MenuOptions.HID,
              menuClass.MenuOptions.IR_BLAST,
              menuClass.MenuOptions.WIFI_SCAN,
              menuClass.MenuOptions.NFC_SUBMENU,
              menuClass.MenuOptions.OS_DETECT,
              menuClass.MenuOptions.HID_ATTACK,
              menuClass.MenuOptions.USB_STATUS,
              menuClass.MenuOptions.SYS_INFO,
              menuClass.MenuOptions.NET_INFO]

    while 1:
        #logging.info("loop")
        if (GPIO.input(config.KEY_SELECT_PIN) == GPIO.LOW):  # noqa: 712
            logging.debug("SELECT Pressed!!!!!!!!!!!!!!!!!!!!!!!")

        if (GPIO.input(config.KEY_UP_PIN) == GPIO.LOW):  # noqa: 712
            logging.debug("UP Pressed!!!!!!!!!!!!!!!!!!!!!!!")
        
        if (GPIO.input(config.KEY_DOWN_PIN) == GPIO.LOW):  # noqa: 712
            logging.debug("DOWN Pressed!!!!!!!!!!!!!!!!!!!!!!!")
        
        if (GPIO.input(config.KEY_CANCEL_PIN) == GPIO.LOW):  # noqa: 712
            logging.debug("CANCEL Pressed!!!!!!!!!!!!!!!!!!!!!!!")

        
        choice = menuClass.start_menu(menu_a, menuClass.MenuType.TEXT)
        time.sleep(0.2)



# bootstrap main method (It's a python thing)
if __name__ == "__main__":
    main()

logging.debug("GPIO.cleanup()")
GPIO.cleanup()
