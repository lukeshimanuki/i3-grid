# uninstall.sh - the uninstaller
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

# check if file exists
if [ -f ${path}/i3-grid ];
then
	# if it exists, try to remove it
	rm /usr/bin/i3-grid
	# check if the file still exists
	if [ -f ${path}/i3-grid ];
	then
		# if it is still there, return an error
		printf "Error: failed to remove ${path}/i3-grid${newline}"
		exit 1
	else
		# otherwise, it was a success
		printf "removed ${path}/i3-grid${newline}"
	fi
else
	# if it does not exists, return an error
	printf "Error: ${path}/i3-grid not found${newline}"
	exit 1
fi
exit 0
