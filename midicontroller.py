#!/usr/bin/env python2

import threading, Queue
import mido
import time
import os
import sys
from subprocess import call, Popen
from config import Config
from oscpy.server import OSCThreadServer


class Midihost(threading.Thread):
    
    def __init__(self, command_q):
        super(Midihost, self).__init__()
        self.command_q = command_q
        self.stoprequest = threading.Event()
        self.osc = None
        

    def send_message(self, received_message):
        print received_message
        self.outputport.send(received_message)

    def stop(self):
        self.outputport.close()
        self.osc.stop()

    def connect_output(self):
        while True:
            try:
                self.outputport = mido.open_output()
                outputs = mido.get_output_names()
                if Config.MIDIOUT:
                    out = [s for s in outputs if Config.MIDIOUT.lower() in s.lower()]
                    if out:
                        self.outputport = mido.open_output(out[0])
                        print "Midi output device connected: " + out[0]
                        break
                    else:
                        raise EnvironmentError
            except EnvironmentError:
                self.outputport.close()
                print "MIDIOUT not found: " + Config.MIDIOUT
                print "Please connect midi device"
                time.sleep(3)        

    def callback(self, path, values=None):
        print "osc: " + path + " : " +str(values)
        message = None
        command = path.split('/')[1]
        if command == "control_change":
            splitted = str(values).split('.')
            value = int(splitted[0])
            message = mido.Message('control_change', channel=Config.MIDICHANNEL-1, control=int(path.split('/')[2]), value=value)
        if command == "program_change":
            message = mido.Message('program_change', channel=Config.MIDICHANNEL-1, program=int(values))
        if command == "control_change_slider":
            message = mido.Message('control_change', channel=Config.MIDICHANNEL-1, control=int(path.split('/')[2]), value=int(values))
        if command == "quit":
            self.command_q.put("KILLSIGNAL")
        if command == "reboot":
            self.command_q.put("REBOOTSIGNAL")
        if command == "restart":
            self.stop()
            print "Restarting..."
            print ""

            os.execv(__file__, sys.argv)
            sys.exit()
        if command == "scroll_preset_up":
            self.callback("/control_change/71", "1.0")
            self.callback("/control_change/50", values)
        if command == "scroll_preset_down":
            self.callback("/control_change/71", "1.0")
            self.callback("/control_change/49", values)

        if message:
            self.send_message(message)


    def run(self):
        self.osc = OSCThreadServer(default_handler=self.callback)
        self.osc.listen(address='0.0.0.0', port=8000, default=True)
        self.connect_output()
        while not self.stoprequest.isSet():
            try:
                message = self.command_q.get(True, 0.05)
                if str(message) == "KILLSIGNAL":
                    Config.shutdown()
                elif str(message) == "REBOOTSIGNAL":
                    Config.reboot()
                else:
                    self.send_message(message)
            except Queue.Empty:
                continue
        self.osc.stop()

    def join(self, timeout=None):
        super(Midihost, self).join(timeout)    

if __name__ == '__main__':
    print mido.get_input_names()
    print mido.get_output_names()
    command_q = Queue.Queue()

    mt = Midihost(command_q = command_q)
    mt.start()

    if 'numpad' in Config.MODULES:
        numpad = MidiNumpad(command_q)
        numpad.start()

    mt.join()

