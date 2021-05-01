#!/bin/bash
killall python
python bootstrapSnowflakeUI.py &
exec $SHELL
