#!/user/bin/env python3

import utility

STATUS_FONT = utility.make_font("Mini Pixel.ttf", 6) #only font readable at status bar sizes
SYMBOL_FONT = utility.make_font("fontawesome-webfont.ttf", 9) #all the utf8 symbols
TEXT_FONT = utility.make_font("miscfs_.ttf", 12) #pretty readable monospace font

LIST_FONT = utility.make_font("FreePixel.ttf", 18) # for the menu lists
JAPAN_FONT = utility.make_font("misaki_gothic.ttf", 12) # supports readable katakana

STATUS_FREQUENCY = 1  # Update one status bar icon per second

# colors for text on screen
FG = "white"
BG = "black"


# Screen Configuration
#width = 128
#height = 64

SCREEN = 0  # SPI mode
#SCREEN = 1  # I2C mode
ROTATION = 2 # 2 for Waveshare 0 for custom
#I2C_ADDRESS = 0x3c

# GPIO define and OLED configuration
RST_PIN = 25  # waveshare SPI settings
DC_PIN = 24  # waveshare SPI settings
#CS_PIN = 8 #CE0

# Waveshare Keys
KEY_CANCEL_PIN = 13 # Key2
KEY_UP_PIN = 21  #  Key1
KEY_DOWN_PIN = 16  #  Key3
KEY_SELECT_PIN =  20 # Stick click 


# Custom Keys
#KEY_CANCEL_PIN = 27
#KEY_UP_PIN = 17
#KEY_DOWN_PIN = 4  
#KEY_SELECT_PIN =  18 
