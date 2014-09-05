# i3-grid.py - the main controller of i3-grid
# 
# Copyright (C) 2014 Luke Shimanuki
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.

import sys

from commands import help, whereami, up, down, right, left, sendUp, sendDown, sendRight, sendLeft

# list of arguments paired with the function to be called
arguments = \
{
        "help" : help,
        "whereami" : whereami,
        "up" : up,
        "down" : down,
        "right" : right,
        "left" : left,
        "sendUp" : sendUp,
        "sendDown" : sendDown,
        "sendRight" : sendRight,
        "sendLeft" : sendLeft
}

# go through each argument (except the first one)
# and call the associated function
for i in range(1, len(sys.argv)):
    arguments[sys.argv[i]]()

# if there were no arguments, print help message
if len(sys.argv) == 1:
    help()

