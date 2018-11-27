import threading, Queue
import mido
import urllib2
import time
from config import Config

class Midihost(threading.Thread):
    
    def __init__(self, command_q):
        super(Midihost, self).__init__()
        self.command_q = command_q
        self.stoprequest = threading.Event()
        

    def send_message(self, received_message):
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


    def run(self):
        self.connect_output()
        while not self.stoprequest.isSet():
            try:
                message = self.command_q.get(True, 0.05)
                print message
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

    def join(self, timeout=None):
        super(Midihost, self).join(timeout)    

if __name__ == '__main__':
    print mido.get_input_names()
    print mido.get_output_names()