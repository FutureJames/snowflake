#!/bin/bash

echo ------------------------------------------------------------------------------------
echo Check IR system files
ls -l /dev/lirc*

echo ------------------------------------------------------------------------------------
echo Show Features avaiable for each lirc device
ir-ctl -d /dev/lirc0 -f
echo 
ir-ctl -d /dev/lirc1 -f

echo ------------------------------------------------------------------------------------
echo Confirm modules loaded
lsmod | grep gpio

echo ------------------------------------------------------------------------------------
echo List devices
cat /proc/bus/input/devices

echo ------------------------------------------------------------------------------------
echo Check ir-keytable configiration
ir-keytable

echo ------------------------------------------------------------------------------------
echo Turn on all protocols
ir-keytable -s rc1 -p lirc,rc-5,rc-5-sz,jvc,sony,nec,sanyo,mce_kbd,rc-6,sharp,xmp

echo -------------------------------------------------------------------------------------
echo Check config again
ir-keytable

echo -------------------------------------------------------------------------------------
echo Start test mode
echo note: Switch 'rc1' to 'rc0' based on the previos config output
#ir-keytable -t -s rc1

echo Recoding to file ir_record
sudo ir-ctl -d /dev/lirc1 -rir_record -v


