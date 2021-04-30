#!/bin/bash

#Battery %
echo 'get battery' | nc -q 1 127.0.0.1 8423
#Bat current in Amp
echo 'get battery_i' | nc -q 1 127.0.0.1 8423
#Bat voltage in Volt
echo 'get battery_v' | nc -q 1 127.0.0.1 8423
#charging status
echo 'get battery_charging' | nc -q 1 127.0.0.1 8423
#get model type
echo 'get model' | nc -q 1 127.0.0.1 8423
#charging LED amount
echo 'get battery_led_amount' | nc -q 1 127.0.0.1 8423
#charging usb plugged
echo 'get battery_power_plugged' | nc -q 1 127.0.0.1 8423
#charging range restart-point & stop-point %
echo 'get battery_charging_range' | nc -q 1 127.0.0.1 8423
#whether cargin is allowed when usb is plugged
echo 'get battery_allow_charging' | nc -q 1 127.0.0.1 8423
echo
#rtc clock
echo 'get rtc_time' | nc -q 1 127.0.0.1 8423
#rtc wakeup alarm enabled
echo 'get rtc_alarm_enabled' | nc -q 1 127.0.0.1 8423
echo
#rtc wakeup alarm repeat in weekdays
echo 'get alarm_repeat' | nc -q 1 127.0.0.1 8423
#get button action
echo 'get button_enable single' | nc -q 1 127.0.0.1 8423
#get button action
echo 'get button_shell single' | nc -q 1 127.0.0.1 8423
#autoshutdown level
echo 'get safe_shutdown_level' | nc -q 1 127.0.0.1 8423
#auto shutdown delay
echo 'get safe_shutdown_delay' | nc -q 1 127.0.0.1 8423



