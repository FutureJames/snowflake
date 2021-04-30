#!/bin/bash
killall python
python runmenu.py &
exec $SHELL
