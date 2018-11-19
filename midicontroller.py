import threading, Queue
import mido
from midinumpad import MidiNumpad,Toggler
import web
import urllib2


MODULES = ('numpad', 'web')
SERVERNAME = '0.0.0.0:5000'

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
                    if 'web' in MODULES:
                        url = "http://"+SERVERNAME+"/quit"
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


def main(args):
    command_q = Queue.Queue()

    mt = Midihost(command_q = command_q)
    mt.start()

    if 'numpad' in MODULES:
        numpad = MidiNumpad(command_q)
        numpad.start()

    if 'web' in MODULES:
        web.start_web(command_q, SERVERNAME)

    mt.join()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])