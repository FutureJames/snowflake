#!/user/bin/env python3
import logging
from enum import Enum
# import datetime
import time
import RPi.GPIO as GPIO  # noqa: N814
# user imports
import setup
import config
import menuText
import menuList
import splashScreen
import displayScreen
import subprocess
import utility
import subprocess

# link back to SetupClass for readability
device = setup.SetupClass.device


# This is the list of all valid menu options
# enum name is used internally for building menu arrays.  should not be changed
# enum value is human readable text for the menus and can be changed any time
# Each of the menu options defined must have an implimentation in executeMenu()
class MenuOptions(Enum):
    NET_INFO = "Network Info"
    SYS_INFO = "System Info"
    WHITE = "subMenu Test"
    HID_ATTACK = "HID Attacks"
    HID = "HID Test"
    USB_STATUS = "USB Gadget Settings"
    SCREEN_OFF = "Screen Off"
    OS_DETECT = "OS Detection"
    WIFI_SCAN = "Wifi Scan"
    NFC_POLL = "NFC Scan"
    NFC_TEST = "NFC Self-Test"
    NFC_CLONE = "NFC Clone"
    NFC_SUBMENU = "NFC Tools    >" 

class MenuType(Enum):
    TEXT = 0
    GRAPHICAL = 1
    LIST = 2

def run_hid(script_name):
    cmd = "P4wnP1_cli hid job '" + script_name + ".js'"
    logging.debug(cmd)
    bash(cmd)
    splashScreen.display(script_name)

# This is the method responsible for launching all menus.  generally called
# from gui.py but also recursivly from executeMenuClass() below
def start_menu(menu, menu_type):
    if (menu_type == MenuType.TEXT):
        response = menuText.display(menu)
        if (response is not None):
            execute_menu_class(menu[response])
        else:
            logging.debug("Menu CANCELLED")
    elif (menu_type == MenuType.LIST):
        response = menuList.display(menu)
        return response
    elif (menu_type == MenuType.GRAPHICAL):
        logging.error("Graphical menu not yet implimented")
    else:
        logging.error("Invalid menu type!")



# helper function for logging and executing simple shell commands
def bash(command):
    try:
        result = subprocess.check_output(command, shell=True)
        logging.info("Executed shell command-> \n" +
                     "                                  " + command + "\n" +
                     "                                  " + result)
    except subprocess.CalledProcessError as e:
        logging.error(e)
        result = None

    return result


# TODO consider moving the actual logic to another class to allow for  reuse
def execute_menu_class(selection):
    logging.info("starting-> execute_menu_class()")

    if (selection == MenuOptions.USB_STATUS):
        logging.debug("exec: USB status Check")
        text = []
        output = subprocess.check_output("P4wnP1_cli usb get", shell=True)
        result = {}
        for row in output.split('\n'):
                if ': ' in row:
                    key, value = row.split(': ')
                    result[key.strip(' .')] = value.strip()
        text.append("Enabled........ " + result['Enabled'])
        if (result['Enabled'] == 'true'):
            text.append("RNDIS.......... " + result['RNDIS'])
            text.append("Mouse.......... " + result['HID Mouse'])
            text.append("Keyboard....... " + result['HID Keyboard'])
            text.append("Mass Storage... " + result['Mass Storage'])
        displayScreen.display(text)

    elif (selection == MenuOptions.HID):
        logging.debug("exec: HID test")
        run_hid("hello_fast")

    elif (selection == MenuOptions.NFC_CLONE):
        # TODO: Add user interface
        logging.debug("exec: NFC Clone")
        displayScreen.display(["Scanning original now", "   please wait..."], False)
        read = bash("nfc-list")
        read = read.splitlines()
        uid = read[5].split(':')[1]
        uid = uid.replace(" ", "")
        logging.info(uid)
        displayScreen.display(["Read in " + uid," ", "Place blank card and", "tap a key to continue"])
        logging.info("Place blank card", "to write")
        #time.sleep(5)
        displayScreen.display(["Writing UID " + uid, "   please wait..." ], False)
        logging.info("Starting write procedure")
        if bash("nfc-mfsetuid " + uid) is not None:
            displayScreen.display(["Clone Complete!"])
        else:
            displayScreen.display(["Error try again"])

    elif (selection == MenuOptions.NFC_TEST):
        logging.debug("exec: NFC TEST")
        displayScreen.display(["Running diagnostic.", "   please wait...",], False)
        nfc = bash("pn53x-diagnose")
        if nfc is not None:
            logging.debug(nfc)
            nfc = nfc.splitlines()
            dev = "Opened  :  " + nfc[1].split(':')[1].split(']')[0]
            com = "COM test: " + nfc[2].split(':')[1]
            ram = "RAM test: " + nfc[4].split(':')[1]
            displayScreen.display([" ===NFC Self Test===", dev, com, ram])
        else:
            displayScreen.display([" ===NFC Self Test===", "FAILED!", "",  "Try a power cycle."])


    elif (selection == MenuOptions.HID_ATTACK):
        path = "/usr/local/P4wnP1/HIDScripts/"
        ext = ".js"
        directory = bash("ls -F --format=single-column " + path + "*" + ext)
        directory = directory.replace(ext, "")
        directory = directory.replace(path, "")
#       directory = directory.replace("*","")
        directory = directory.split("\n")
        response = start_menu(directory, MenuType.LIST)
        if (response is not None):
            run_hid(directory[response])

    elif (selection == MenuOptions.NFC_POLL):
        logging.debug("exec: NFC_POLL")
        displayScreen.display(["Place on NFC/RFID.","", "    scanning..."], False)
        nfc = bash("nfc-list")
        #nfc = bash("nfc-poll")
        nfc = nfc.splitlines()
        if (len(nfc) > 2):
            atqa = "ATAQ: " + nfc[4].lstrip().split(':')[1]
            uid = "UID : " + nfc[5].lstrip().split(':')[1]
            sak = "SAK : "+ nfc[6].lstrip().split(':')[1]
            # logging.debug(nfc)
            #logging.info(str(uid), str(atqa), str(sak))
            displayScreen.display(["==NFC Scan Complete=="," " ,uid, atqa, sak])
        else:
            displayScreen.display(["Scan failed :(","",  "Try placing card", "  more quickly"])


    # Network Info
    elif (selection == MenuOptions.NET_INFO):
        logging.debug("exec: NET_INFO")
        ip_wifi = bash("hostname -I | cut -d\' \' -f1")
        ip_usb = bash("hostname -I | cut -d\' \' -f2")
        ip_bt = bash("hostname -I | cut -d\' \' -f3")
        displayScreen.display(["Network Info",
                               "Wifi: " + ip_wifi,
                               "USB : " + ip_usb,
                               "BT  : " + ip_bt])

    # Device Info Screen
    elif (selection == MenuOptions.SYS_INFO):
        logging.debug("exec: SYS_INFO")
        column = str(15)  # set column gap
        # now = datetime.datetime.now()
        # time_format = "{0:" + column + "s}{1:s}"
        # time = time_format.format(now.strftime("%H:%M:%S"),
        #                          now.strftime("%d:%b:%y"))
        batt = bash("echo get battery \
                    | nc -q 1 127.0.0.1 8423 \
                    | awk '{printf\"%-"+column+"s%.0f%%\", \"Battery:\", $2}'")
        temp = bash("cat /sys/class/thermal/thermal_zone0/temp \
                    | awk '{printf \"%-"+column+"s%.0fC\", \"Temp:\", $1/1000}'")  # noqa: 501
        cpu = bash("top -bn1 | grep %Cpu | awk '{printf \"%-"+column+"s%.0f%%\", \"CPU:\" ,$2}'")  # noqa: 501
        mem = bash("free -m | awk 'NR==2{printf \"%-"+column+"s%.0f%%\", \"MEM:\", $3*100/$2}'")  # noqa: 501
        disk = bash("df -h | awk '$NF==\"/\"{printf \"%-"+column+"s%d/%dGB %s\",\"Disk:\", $3,$2,$5}'")  # noqa: 501
        displayScreen.display([batt, temp, cpu, mem, disk])

    elif (selection == MenuOptions.WHITE):
        logging.debug("exec: submenu")
        menu_b = [MenuOptions.USBSTATUS, MenuOptions.SYSINFO]
        start_menu(menu_b, MenuType.TEXT)

    elif (selection == MenuOptions.NFC_SUBMENU):
        logging.debug("exec: NFC_SUBMENU")
        menu_b = [MenuOptions.NFC_POLL, MenuOptions.NFC_CLONE, MenuOptions.NFC_TEST]
        start_menu(menu_b, MenuType.TEXT)

    elif (selection == MenuOptions.SCREEN_OFF):
        time.sleep(0.2)
        logging.debug("screen sleeping zzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        while GPIO.input(config.KEY_SELECT_PIN ):
            device.hide()
            time.sleep(0.1)
        logging.debug("Screen waking up")
        device.show()

    elif (selection == MenuOptions.OS_DETECT):
        time.sleep(0.2)
        displayScreen.display(["Scanning OS with nMap", "please wait...",], False)
        logging.debug("OS Detection starting")
        os = bash("nmap -p 22,80,445,65123,56123 -O 172.16.0.2 | grep Running | cut -d ':' -f2")
        if (os):  # DEBUG: this can probably be moved to the displayScreen
            lineLength = 21
            chunks = [os[i:i+lineLength] for i in range(0, len(os), lineLength)]
            logging.info("OS detected as :" + os)
            logging.debug(chunks)
            displayScreen.display(["OS Detected as:"] + chunks)
        else:
            displayScreen.display(["Host down or", "  not connected"])

    elif (selection == MenuOptions.WIFI_SCAN):
        time.sleep(0.2)
        displayScreen.display(["Wifi Scanning...", "please wait"], False)
        logging.debug("Wifi Scan starting")
        scan = bash("iwlist wlan0 scan | grep ESSID | awk {'print $NF'} | cut -d ':' -f2 | cut -d '\"' -f2")
        # cleaup up list...
        scan = scan.split("\n")
        while("" in scan):
             scan.remove("")
        # ...and remove duplicates
        scan = list(set(scan))
        logging.info(scan)
        start_menu(scan, MenuType.LIST)

    else:
        logging.error("executeMenuClass-> UNKNOWN menu option: "
                      + selection.value)
