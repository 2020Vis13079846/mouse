#!/usr/bin/env python

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

import json
import os
import core.helper as h
import re

class command:
	def __init__(self):
		self.name = "download"
		self.description = "Download remote file."
		self.usage = "Usage: download <remote_path> <local_path>"
		self.type = "native"

	def run(self,session,cmd_data):
		if len(cmd_data['args'].split()) < 1:
            		print self.usage
            		return

                if len(cmd_data['args'].split()) < 2:
                        print self.usage
                        return
		
		w = os.environ['OLDPWD']
            	os.chdir(w)
		
		remote_path = os.path.split(cmd_data['args'].split()[0])[-1]
		local_path = cmd_data['args'].split()[1]
		h.info_general("Downloading {0}...".format(cmd_data['args'].split()[0]))
		data = session.download_file(cmd_data['args'].split()[0])
		if data:
			# save to downloads
			h.info_general("Saving {0}...".format(cmd_data['args'].split()[0]))
			f = open(os.path.join(local_path,remote_path),'w')
			f.write(data)
			f.close()
			saved = os.path.join(local_path,remote_path)
			h.info_success("Saved to "+saved+"!")
		g = os.environ['HOME']
            	os.chdir(g + "/mouse")
