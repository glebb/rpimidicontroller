import platform
from subprocess import call

class BaseConfig:
    MIDIOUT = ''
    MIDIIN = 'LPD'
    MODULES = ('')
    MIDICHANNEL = 1
    NUMPAD_MODE_CHANGE_SCANCODES = (69,98,55)
    NUMPAD_KILLSIGNAL = "987" #trigger always 0
    NUMPAD_PREVSCANCODE = 82
    NUMPAD_NEXTSCANCODE = 76

    @staticmethod
    def shutdown():
        print 'shutdown...'

    @staticmethod
    def reboot():
        print 'reboot...'


class Linux(BaseConfig):
    MIDIOUT = 'Stomp'
    NUMPAD_MODE_CHANGE_SCANCODES = (69,98,55) # numlock / *
    NUMPAD_PREVSCANCODE = 82
    NUMPAD_NEXTSCANCODE = 76

    @staticmethod
    def shutdown():
        call("echo heartbeat | sudo tee /sys/class/leds/led0/trigger", shell=True)
        call("echo heartbeat | sudo tee /sys/class/leds/led1/trigger", shell=True)
        call("sudo shutdown -h now", shell=True)

    @staticmethod
    def reboot():
        call("echo heartbeat | sudo tee /sys/class/leds/led0/trigger", shell=True)
        call("echo heartbeat | sudo tee /sys/class/leds/led1/trigger", shell=True)
        call("sudo shutdown -r now", shell=True)

class Darwin(BaseConfig):
    NUMPAD_MODE_CHANGE_SCANCODES = (65,75,67) # , / *
    MIDIOUT = 'IAC-ajuri'

class Windows(BaseConfig):
    pass

Config = eval(platform.system())