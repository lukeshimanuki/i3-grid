# install.sh - the installer
# 
# Copyright (C) 2014 Luke Shimanuki
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.

# define the installation path
path="/usr/bin"

# automatically abort on error
set -e

# define a newline variable for maximum portability
newline="$(printf '\nX')"
newline="${newline%X}"

# check if file already exists
if [ -f "${path}/i3-grid" ];
then
	# if it already exists, return an error
	printf "Error: ${path}/i3-grid already exists${newline}"
	exit 1
else
	# if not, try to install the file
	# this is the contents of the shell script to be installed into /usr/bin
	script="#!/bin/sh${newline}export IFS=' '${newline}python $(pwd)/i3-grid.py \$*${newline}"
	# copy the script over and make it executable
	printf "${script}" > ${path}/i3-grid
	chmod +x ${path}/i3-grid
	# check if file exists and is executable
	if [ -f "${path}/i3-grid" ];
	then
		if [ -x "${path}/i3-grid" ];
		then
			# print success
			printf "${script}${newline}has been saved to /usr/bin/i3-grid${newline}"
		else
			# return an error
			printf "Error: failed to make ${path}/i3-grid executable${newline}"
			exit 1
		fi
	else
		# return an error
		printf "Error: failed to install ${path}/i3-grid${newline}"
		exit 1
	fi
fi
exit 0
