# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    installer.sh                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lgaultie <lgaultie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 09:58:45 by lgaultie          #+#    #+#              #
#    Updated: 2019/11/06 10:20:13 by lgaultie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# a faire: silence linstallation de miniconda

#!/usr/bin/env bash

remove_python()
{
	# change path to miniconda directory
	rm -rf /Users/lgaultie/goinfre/miniconda
	echo Python has been removed.
}

install_python()
{
	# https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html
	# change path to dowloaded Miniconda file
	bash /Users/lgaultie/goinfre/Miniconda3-latest-MacOSX-x86_64.sh -b -p /Users/lgaultie/goinfre/miniconda > /dev/null
	# change path of new miniconda directory and .zshrc file
	echo "export PATH="/Users/lgaultie/goinfre/miniconda/bin:$PATH"" >> ~/.zshrc
	echo python has been installed.
}

check_if_installed()
{
	echo Python 3 is already installed, do you want to reinstall it ? [yes/no]
	read choice
	if [ $choice = "Yes" ] || [ $choice = "yes" ] || [ $choice = "y" ]; then
		remove_python
		install_python
	fi
}

if [ "$(python -V)" = "Python 3.7.4" ]; then
	check_if_installed
else
	install_python
fi
