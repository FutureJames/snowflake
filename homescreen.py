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

    menu_a = [menuClass.MenuOptions.HID,
              menuClass.MenuOptions.WIFI_SCAN,
              menuClass.MenuOptions.NFC_CLONE,
              menuClass.MenuOptions.NFC_TEST,
              menuClass.MenuOptions.NFC_POLL,
              menuClass.MenuOptions.OS_DETECT,
              menuClass.MenuOptions.HID_ATTACK,
              menuClass.MenuOptions.SCREEN_OFF,
              menuClass.MenuOptions.USB_STATUS,
              menuClass.MenuOptions.SYS_INFO,
              menuClass.MenuOptions.NET_INFO]

    while 1:
        choice = menuClass.start_menu(menu_a, menuClass.MenuType.TEXT)
        time.sleep(0.2)



# bootstrap main method (It's a python thing)
if __name__ == "__main__":
    main()

logging.debug("GPIO.cleanup()")
GPIO.cleanup()
