#!/bin/bash

#helper for basic libnfc commands for testing PN532
# https://www.mankier.com/package/libnfc-examples
echo i2cdetect is a userspace program to scan an I2C bus for devices 
i2cdetect -y 1
echo

echo pn53x-diagnose
pn53x-diagnose
echo

echo nfc-list is a utility for listing any available device compliant with libnfc
nfc-scan-device -v
echo 

echo nfc-scan-device is a utility for listing any available tags like ISO14443-A, FeliCa, Jewel or ISO14443-B according to the device capabilities
nfc-list -v
echo

#echo nfc-poll is a utility for polling any available target, tags but also NFCIP targets, using ISO14443-A, FeliCa, Jewel and ISO14443-B modulations.
#nfc-poll -v


