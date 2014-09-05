# commands.py - usable commands that are to be invoked by i3-grid.py
# 
# Copyright (C) 2014 Luke Shimanuki
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.

from config import moveWithSend, rows, cols

from subprocess import Popen, PIPE

# converts coordinates to id
def _getID(row, col):
    return cols * row + col

# converts id to coordinates
def _getCoord(ID):
    return int(ID / cols), ID % cols

# moves to a workspace
def _move(ID):
    Popen(["i3-msg", "workspace", str(ID)], stdout = PIPE).communicate()

# sends window to a workspace
def _send(ID):
    Popen(["i3-msg", "move", "container", "to", "workspace", str(ID)], stdout = PIPE).communicate()
    if moveWithSend:
        _move(ID)

# determines the id of the current workspace
def _getCurrentWorkspace():
    # grab i3's list of workspaces
    workspaces = str(Popen(["i3-msg", "-t", "get_workspaces"], stdout = PIPE).communicate()[0])
    # find the "focused"
    focused = workspaces.find('"focused":true')
    if focused == -1:
        return 0
    # find the "num" closest to the left of the "focused"
    num = workspaces.rfind('"num":', 0, focused)
    if num == -1:
        return 0
    # the number starts 6 bytes after the "num"
    start = num + 6
    # the number ends at the comma
    end = workspaces.find(',', start)
    if end == -1:
        return 0
    # turn into int
    return int(workspaces[start : end])


# print help message
def help():
    helpMessage = \
    (
        "i3-grid - a gridded workspace manager for the i3 window manager\n"
        "Copyright (C) 2014 Luke Shimanuki\n"
        "Version 1.0\n"
        "\n"
        "This program is open source and is licensed under the GNU Public License Version\n"
        "3 (GPLv3). That means anyone may freely use it, distribute it, or modify it as\n"
        "long as you declare any changes and release modified works under the GPL. More\n"
        "officially:\n"
        "\n"
        "This program is free software: you can redistribute it and/or modify\n"
        "it under the terms of the GNU General Public License as published by\n"
        "the Free Software Foundation, either version 3 of the License, or\n"
        "(at your option) any later version.\n"
        "\n"
        "This program is distributed in the hope that it will be useful,\n"
        "but WITHOUT ANY WARRANTY; without even the implied warranty of\n"
        "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n"
        "GNU General Public License for more details.\n"
        "\n"
        "You should have received a copy of the GNU General Public License\n"
        "along with this program.  If not, see <http://www.gnu.org/licenses/>.\n"
        "\n"
        "Syntax: i3-grid <commands>\n"
        "To use with i3: bindsym <key> exec /path/to/i3-grid <command>\n"
        "\n"
        "Usable Commands:\n"
        "help      | prints this help message\n"
        "whereami  | prints the current workspace\n"
        "          |\n"
        "up        | moves up\n"
        "down      | moves down\n"
        "left      | moves left\n"
        "right     | moves right\n"
        "          |\n"
        "sendUp    | sends window up\n"
        "sendDown  | sends window down\n"
        "sendRight | sends window right\n"
        "sendLeft  | sends window left\n"
    );
    print(helpMessage)

# print current workspace
def whereami():
    workspace = _getCurrentWorkspace()
    print('(' + str(_getCoord(workspace)[0]) + ', ' + str(_getCoord(workspace)[1]) + ')')

# move in direction
def up():
    row, col = _getCoord(_getCurrentWorkspace())
    if row - 1 >= 0:
        _move(_getID(row - 1, col))
def down():
    row, col = _getCoord(_getCurrentWorkspace())
    if row + 1 < rows:
        _move(_getID(row + 1, col))
def right():
    row, col = _getCoord(_getCurrentWorkspace())
    if col + 1 < cols:
        _move(_getID(row, col + 1))
def left():
    row, col = _getCoord(_getCurrentWorkspace())
    if col - 1 >= 0:
        _move(_getID(row, col - 1))

# send window in direction
def sendUp():
    row, col = _getCoord(_getCurrentWorkspace())
    if row - 1 >= 0:
        _send(_getID(row - 1, col))
def sendDown():
    row, col = _getCoord(_getCurrentWorkspace())
    if row + 1 < rows:
        _send(_getID(row + 1, col))
def sendRight():
    row, col = _getCoord(_getCurrentWorkspace())
    if col + 1 < cols:
        _send(_getID(row, col + 1))
def sendLeft():
    row, col = _getCoord(_getCurrentWorkspace())
    if col - 1 >= 0:
        _send(_getID(row, col - 1))

