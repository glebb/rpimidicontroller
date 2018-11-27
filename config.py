import platform
from subprocess import call

class BaseConfig:
    MODULES = ('web')
    SERVERNAME = '0.0.0.0:5000'
    MIDICHANNEL = 1
    NUMPAD_MODE_CHANGE_SCANCODES = (69,98,55)
    NUMPAD_KILLSIGNAL = "987" #trigger always 0
    NUMPAD_PREVSCANCODE = 82
    NUMPAD_NEXTSCANCODE = 76
    MIDIOUT = 'HX Stomp'
    MIDIIN = 'LPD 8'

    @staticmethod
    def shutdown():
        pass

class Linux(BaseConfig):
    SERVERNAME = '0.0.0.0:80'
    NUMPAD_MODE_CHANGE_SCANCODES = (69,98,55) # numlock / *
    NUMPAD_PREVSCANCODE = 82
    NUMPAD_NEXTSCANCODE = 76
    MIDIOUT = 'HX Stomp:HX Stomp MIDI 1 20:0'

    @staticmethod
    def shutdown():
        call("echo heartbeat | sudo tee /sys/class/leds/led0/trigger", shell=True)
        call("echo heartbeat | sudo tee /sys/class/leds/led1/trigger", shell=True)
        call("sudo shutdown -h now", shell=True)


class Darwin(BaseConfig):
    MODULES = ('web')
    NUMPAD_MODE_CHANGE_SCANCODES = (65,75,67) # , / *
    @staticmethod
    def shutdown():
        print "quitting"
    pass

class Windows(BaseConfig):
    pass

Config = eval(platform.system())