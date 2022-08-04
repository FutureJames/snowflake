#!/user/bin/env python3
# -*- coding:utf-8 -*-
"""Docstring"""
from __future__ import unicode_literals
import logging
import subprocess
import commands
#import subprocess
from subprocess import Popen, PIPE
# import user classes
import config
import setup
import utility


# link back to SetupClass for readability
device = setup.SetupClass.device

# icon to use for testing/layout EMPTY status indicators
EMPTY = ""  # "\uf068"


# helper to intialize lists in calling classes
def init():
    return [0, 0, 0, 0, 0, 0]

# HELPER FUNCTIONS #########################


# detect which mode wifi is in
def get_wifi_status():
    if utility.bash("iwconfig wlan0 | grep 'ESSID:off/any'") is not None:
        return 1  # wifi off
    if utility.bash("iwconfig wlan0 | grep 'Mode:Master'") is not None:
        return 2  # AP mode
    if utility.bash("iwconfig wlan0 | grep 'Mode:Managed'") is not None:
        return 3  # client mode
    # else:
    return 0  # something unexpected


# detect charging cable
def get_battery_charging():
    charge = utility.bash("echo 'get battery_power_plugged' \
                    | nc -q 1 127.0.0.1 8423 \
                    | awk '{printf \"%s\",$2}'")
    if charge == "true":
        return True
    else:
        return False


# get battery percent
def get_battery_capacity():
    batt = utility.bash("echo get battery \
                | nc -q 1 127.0.0.1 8423 \
                | awk '{printf \"%.0f\", $2 }'")
    return int(batt)

# detect if USB-OTG is connected to computer
def get_usb_status():
    #logging.debug("GETTING USB STATUS")
    # There is a spelling error in the dmesg logs so just the first letter
    # should be more durable over patches
    # -->  "New USB Geadget connect state:"
    plugged = utility.bash("tac /var/log/messages \
                            | grep -a -m 1 'New USB G' \
                            | awk {'print $NF'}")
    # Check if response is null or empty
    # TODO: update this to deal with logrotate for var/log/messages
    if (plugged is not None) and (plugged):
        plugged = bool(int(plugged))
    else:
        plugged = 0

    enabled = utility.bash("P4wnP1_cli usb get \
                    | grep -a  'Enabled:      true'")
    enabled = bool(enabled)

    return plugged and enabled


def get_usb_ethernet_status():
    usbeth = utility.bash("tac /var/log/messages | grep -a -m 1 'usbeth:' | grep 'forwarding'")
    #logging.debug(usbeth)
    if usbeth == None:
        return False
    else:
        return True

# RENDERING FUNCTIONS ################################


def get_icon_wifi_status(state):
    wifi_icon = [EMPTY, EMPTY,  "\uf1eb", "\uf012"]
    return wifi_icon[state]


def get_icon_battery(battery_capacity):
    battery_icon = ["\uf244", "\uf243", "\uf242", "\uf241", "\uf240"]
    # choose correct icon based on capacity remaining
    if (battery_capacity >= 0 and battery_capacity < 5):
        return battery_icon[0]
    elif (battery_capacity >= 5 and battery_capacity < 35):
        return battery_icon[1]
    elif (battery_capacity >= 35 and battery_capacity < 50):
        return battery_icon[2]
    elif (battery_capacity >= 50 and battery_capacity < 75):
        return battery_icon[3]
    elif (battery_capacity >= 75 and battery_capacity <= 100):
        return battery_icon[4]
    else:
        return EMPTY


def get_icon_charging(status):
    charge_icon = [EMPTY, "\uf0e7"]
    if status:
        return charge_icon[1]
    else:
        return charge_icon[0]


def get_icon_usb_status(status):
    usb_icon = [EMPTY, "\uf287"]
    if status:
        return usb_icon[1]
    else:
        return usb_icon[0]


def get_icon_usb_ethernet(status):
    ether_icon = [EMPTY, "\uf0e8"]  # \uf062
    if status:
        return ether_icon[1]
    else:
        return ether_icon[0]


def get_status_icons(status):
    # logging.debug(len(status))
    active = status[0]
    wifi = get_icon_wifi_status(status[1])
    charge = get_icon_charging(status[2])
    batt = get_icon_battery(status[3])
    usb = get_icon_usb_status(status[4])
    ether = get_icon_usb_ethernet(status[5])
    return [active, wifi, charge, batt, usb, ether]


def get_status(status):
    wifi_status = status[1]
    battery_charging = status[2]
    battery_capacity = status[3]
    usb_status = status[4]
    ethernet_status = status[5]

    # increment which item we are updating
    if status[0] < len(status)-1:
        status[0] += 1
    else:
        status[0] = 1
    active = status[0]

    # refreshing at the configured frequency to reduce CPU swamping
    if active == 1:
        battery_capacity = get_battery_capacity()
    elif active == 2:
        battery_charging = get_battery_charging()
    elif active == 3:
        usb_status = get_usb_status()
    elif active == 4:
        wifi_status = get_wifi_status()
    elif active == 5:
        ethernet_status = get_usb_ethernet_status()
    else:
        logging.error("getStatusValues conditional broken, "
                      + "updating BATTERY status instead")
        battery_capacity = get_battery_capacity()

    return [active, wifi_status, battery_charging,
            battery_capacity, usb_status, ethernet_status]


# main entry to the class.  Used by the menus to facilitate
# displaying the status bar
def draw(draw, status_values):
    status_icons = get_status_icons(status_values)
    draw.text((0, 0),
              text=status_icons[1],
              font=config.SYMBOL_FONT,
              fill=config.FG)  # wifi
    draw.text((96, 0),
              text=status_icons[2],
              font=config.SYMBOL_FONT,
              fill=config.FG)  # chrg
    draw.text((116, 0),
              text=status_icons[3],
              font=config.SYMBOL_FONT,
              fill=config.FG)  # batt
    draw.text((12, 0),
              text=status_icons[4],
              font=config.SYMBOL_FONT,
              fill=config.FG)  # usb
    draw.text((25, 0),
              text=status_icons[5],
              font=config.SYMBOL_FONT,
              fill=config.FG)  # ether
    draw.text((102, 0),
              text=str(status_values[3]) + "%",
              font=config.STATUS_FONT,
              fill=config.FG)  # batt%
