import threading, Queue
import mido
import urllib2
from subprocess import call
from config import Config
class Midihost(threading.Thread):
    def __init__(self, command_q):
        super(Midihost, self).__init__()
        self.command_q = command_q
        self.stoprequest = threading.Event()
        self.outputport = mido.open_output()

    def send_message(self, received_message):
        self.outputport.send(received_message)

    def stop(self):
        self.outputport.close()

    def run(self):
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
