#!/user/bin/env python3

import utility

STATUS_FONT = utility.make_font("Mini Pixel.ttf", 6) #only font readable at status bar sizes
SYMBOL_FONT = utility.make_font("fontawesome-webfont.ttf", 9) #all the utf8 symbols
#TEXT_FONT = utility.make_font("FreePixel.ttf", 10) #this was what we were using 
TEXT_FONT = utility.make_font("miscfs_.ttf", 12) #pretty readable monospace font

LIST_FONT = utility.make_font("FreePixel.ttf", 18) # for the menu lists
JAPAN_FONT = utility.make_font("misaki_gothic.ttf", 12) # supports readable katakana

STATUS_FREQUENCY = 1  # Update one status bar icon per second 

# colors for text on screen
FG = "white"
BG = "black"

# GPIO define and OLED configuration
RST_PIN = 25  # waveshare settings
CS_PIN = 8   # waveshare settings
DC_PIN = 24  # waveshare settings
KEY_UP_PIN = 21  # 6  #stick up
KEY_DOWN_PIN = 16  # 19 #stick down
KEY_LEFT_PIN = 13  # 5  #sitck left // go back
KEY_RIGHT_PIN = 20  # 26 #stick right // go in // validate
KEY_PRESS_PIN = 13  # stick center button
KEY1_PIN = 21  # key 1 // up
KEY2_PIN = 20  # 20 #key 2 // cancel/goback
KEY3_PIN = 16  # key 3 // down
USER_I2C = 0   # set to 1 if your oled is I2C or 0 if use SPI interface
