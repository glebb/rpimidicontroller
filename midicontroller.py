import threading, Queue
import mido
import urllib2
import time
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

    def connect_output(self):
        while True:
            try:
                self.outputport = mido.open_output()
                outputs = mido.get_output_names()
                out = [s for s in outputs if Config.MIDIOUT.lower() in s.lower()]
                if out:
                    self.outputport = mido.open_output(out[0])
                    print "Midi device connected: " + Config.MIDIOUT
                    break
                else:
                    raise EnvironmentError
            except EnvironmentError:
                self.outputport.close()
                print "MIDIOUT not found: " + Config.MIDIOUT
                print "Please connect midi device"
                time.sleep(3)        

    def callback(self, path, values=None):
        message = None
        command = path.split('/')[1]
        if command == "control_change":
            print values
            splitted = str(values).split('.')
            value = int(splitted[0])
            message = mido.Message('control_change', channel=Config.MIDICHANNEL-1, control=int(path.split('/')[2]), value=value)
        if command == "program_change":
            message = mido.Message('program_change', channel=Config.MIDICHANNEL-1, program=int(values))
        if command == "control_change_slider":
            message = mido.Message('control_change', channel=Config.MIDICHANNEL-1, control=int(path.split('/')[2]), value=int(values))
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
                    url = "http://"+Config.SERVERNAME+"/quit"
                    try:
                        content = urllib2.urlopen(url).read()
                    except:
                        pass
                    self.stoprequest.set()
                else:
                    self.send_message(message)
            except Queue.Empty:
                continue
        self.osc.stop()

    def join(self, timeout=None):
        self.stoprequest.set()
        super(Midihost, self).join(timeout)    

if __name__ == '__main__':
    print mido.get_input_names()
    print mido.get_output_names()